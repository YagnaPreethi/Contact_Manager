
"""JSON persistence for contacts."""

import json
from pathlib import Path
from typing import Protocol

from contact_app.models.contact import Contact


class ContactRepository(Protocol):
    """Define the storage operations required by the service."""

    def list_all(self) -> list[Contact]: ...
    def get_by_id(self, contact_id: str) -> Contact | None: ...
    def save(self, contact: Contact) -> None: ...
    def delete(self, contact_id: str) -> None: ...


class JsonContactRepository:
    """Store contacts in a JSON file."""

    def __init__(self, file_path: Path | str) -> None:
        self.file_path = Path(file_path)

    def list_all(self) -> list[Contact]:
        """Load all contacts from JSON."""
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(
                "The contacts file contains invalid JSON."
            ) from error

        if not isinstance(data, list):
            raise ValueError("Contact data must be a list.")

        contacts: list[Contact] = []
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Each stored contact must be an object.")
            try:
                contacts.append(Contact.from_dict(item))
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(
                    "A stored contact contains invalid data."
                ) from error

        return contacts

    def get_by_id(self, contact_id: str) -> Contact | None:
        """Find a contact by its unique ID."""
        for contact in self.list_all():
            if contact.contact_id == contact_id:
                return contact
        return None

    def save(self, contact: Contact) -> None:
        """Insert or replace a contact by ID."""
        contacts = self.list_all()

        for index, existing in enumerate(contacts):
            if existing.contact_id == contact.contact_id:
                contacts[index] = contact
                break
        else:
            contacts.append(contact)

        self._write(contacts)

    def delete(self, contact_id: str) -> None:
        """Delete a contact by ID."""
        contacts = self.list_all()
        remaining = [
            contact for contact in contacts
            if contact.contact_id != contact_id
        ]

        if len(remaining) == len(contacts):
            return

        self._write(remaining)

    def _write(self, contacts: list[Contact]) -> None:
        """Write the contact list to JSON."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                [contact.to_dict() for contact in contacts],
                file,
                indent=4,
            )