

"""JSON persistence with validation and atomic file replacement."""

import json
import os
import tempfile
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
    """Store contacts in a validated JSON file."""

    def __init__(self, file_path: Path | str) -> None:
        self.file_path = Path(file_path)

    def list_all(self) -> list[Contact]:
        """Load and validate all records in deterministic order."""
        if not self.file_path.exists():
            return []

        try:
            content = self.file_path.read_text(encoding="utf-8")
        except OSError as error:
            raise ValueError("Unable to read the contacts file.") from error

        if not content.strip():
            raise ValueError("The contacts file is empty and cannot be read.")

        try:
            data = json.loads(content)
        except json.JSONDecodeError as error:
            raise ValueError(
                "The contacts file contains invalid JSON."
            ) from error

        if not isinstance(data, list):
            raise ValueError("Contact data must be a JSON list.")

        contacts: list[Contact] = []
        seen_ids: set[str] = set()

        for index, item in enumerate(data):
            if not isinstance(item, dict):
                raise ValueError(
                    f"Contact record {index + 1} must be a JSON object."
                )

            if not isinstance(item.get("name"), str):
                raise ValueError(
                    f"Contact record {index + 1} has an invalid name."
                )

            if not isinstance(item.get("phone"), str):
                raise ValueError(
                    f"Contact record {index + 1} has an invalid phone."
                )

            if not isinstance(item.get("email", ""), str):
                raise ValueError(
                    f"Contact record {index + 1} has an invalid email."
                )

            contact_id = item.get("contact_id")

            if contact_id is not None and (
                not isinstance(contact_id, str) or not contact_id.strip()
            ):
                raise ValueError(
                    f"Contact record {index + 1} has an invalid ID."
                )

            try:
                contact = Contact.from_dict(item)
            except (KeyError, TypeError, ValueError, AttributeError) as error:
                raise ValueError(
                    f"Contact record {index + 1} contains invalid data."
                ) from error

            if contact.contact_id in seen_ids:
                raise ValueError(
                    f"Duplicate contact ID found: {contact.contact_id}"
                )

            seen_ids.add(contact.contact_id)
            contacts.append(contact)

        # Sorting by ID gives a stable order across repeated reads.
        return sorted(contacts, key=lambda contact: contact.contact_id)

    def get_by_id(self, contact_id: str) -> Contact | None:
        """Find a contact by ID."""
        for contact in self.list_all():
            if contact.contact_id == contact_id:
                return contact
        return None

    def save(self, contact: Contact) -> None:
        """Insert or update a contact, rejecting duplicate IDs."""
        contacts = self.list_all()
        matching_index = next(
            (
                index for index, existing in enumerate(contacts)
                if existing.contact_id == contact.contact_id
            ),
            None,
        )

        if matching_index is not None:
            contacts[matching_index] = contact
        else:
            contacts.append(contact)

        self._write(contacts)

    def delete(self, contact_id: str) -> None:
        """Delete an existing contact by ID."""
        contacts = self.list_all()
        remaining = [
            contact for contact in contacts
            if contact.contact_id != contact_id
        ]

        if len(remaining) == len(contacts):
            return

        self._write(remaining)

    def _write(self, contacts: list[Contact]) -> None:
        """Write JSON to a temporary file and atomically replace the target."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path: str | None = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.file_path.parent,
                prefix=f".{self.file_path.name}.",
                suffix=".tmp",
                delete=False,
            ) as temp_file:
                temp_path = temp_file.name
                json.dump(
                    [
                        contact.to_dict()
                        for contact in sorted(
                            contacts,
                            key=lambda item: item.contact_id,
                        )
                    ],
                    temp_file,
                    indent=4,
                    ensure_ascii=False,
                )
                temp_file.write("\n")
                temp_file.flush()
                os.fsync(temp_file.fileno())

            os.replace(temp_path, self.file_path)
            temp_path = None

        except (OSError, TypeError, ValueError) as error:
            raise ValueError("Unable to safely save contacts.") from error

        finally:
            if temp_path is not None:
                try:
                    os.unlink(temp_path)
                except FileNotFoundError:
                    pass
