
"""Business logic for Contact Manager."""

from contact_app.exceptions import (
    ContactNotFoundError,
    DuplicateContactError,
    InvalidContactError,
)
from contact_app.models.contact import Contact
from contact_app.persistence.json_contact_repository import ContactRepository


class ContactService:
    """Provide CRUD operations for contacts."""

    def __init__(self, repository: ContactRepository) -> None:
        """Receive the repository used to store contacts."""
        self.repository = repository

    def create_contact(
        self, name: str, phone: str, email: str = ""
    ) -> Contact:
        """Create and persist a contact."""
        self._validate_fields(name, phone, email)

        if any(c.phone == phone.strip()
               for c in self.repository.list_all()):
            raise DuplicateContactError(
                "This phone number already exists."
            )

        try:
            contact = Contact(name=name, phone=phone, email=email)
        except (AttributeError, ValueError) as error:
            raise InvalidContactError(str(error)) from error

        self.repository.save(contact)
        return contact

    def list_contacts(self) -> list[Contact]:
        """Return all contacts."""
        return self.repository.list_all()

    def get_contact(self, contact_id: str) -> Contact:
        """Retrieve a contact by its unique ID."""
        contact = self.repository.get_by_id(contact_id)

        if contact is None:
            raise ContactNotFoundError(
                f"Contact with ID '{contact_id}' was not found."
            )

        return contact

    def update_contact(
        self,
        contact_id: str,
        name: str | None = None,
        phone: str | None = None,
        email: str | None = None,
    ) -> Contact:
        """Update and persist an existing contact."""
        contact = self.get_contact(contact_id)

        new_name = contact.name if name is None else name
        new_phone = contact.phone if phone is None else phone
        new_email = contact.email if email is None else email

        self._validate_fields(new_name, new_phone, new_email)

        for other in self.repository.list_all():
            if (
                other.contact_id != contact_id
                and other.phone == new_phone.strip()
            ):
                raise DuplicateContactError(
                    "This phone number already exists."
                )

        try:
            contact.update_details(name, phone, email)
        except (AttributeError, ValueError) as error:
            raise InvalidContactError(str(error)) from error

        self.repository.save(contact)
        return contact

    def delete_contact(self, contact_id: str) -> None:
        """Delete an existing contact."""
        self.get_contact(contact_id)
        self.repository.delete(contact_id)

    @staticmethod
    def _validate_fields(
        name: str, phone: str, email: str
    ) -> None:
        """Validate required fields and their basic types."""
        if not all(isinstance(value, str) for value in (name, phone, email)):
            raise InvalidContactError(
                "Name, phone, and email must be text."
            )
        if not name.strip():
            raise InvalidContactError("Name is required.")
        if not phone.strip():
            raise InvalidContactError("Phone number is required.")
