# """Domain model for a contact."""

# from dataclasses import dataclass, field
# from datetime import datetime, timezone
# from uuid import uuid4


# @dataclass
# class Contact:
#     """Represent one contact in the Contact Manager."""

#     name: str
#     phone: str
#     email: str = ""
#     contact_id: str = field(default_factory=lambda: str(uuid4()))
#     created_at: datetime = field(
#         default_factory=lambda: datetime.now(timezone.utc)
#     )

#     def __post_init__(self) -> None:
#         """Validate required contact fields after initialization."""
#         self.name = self.name.strip()
#         self.phone = self.phone.strip()
#         self.email = self.email.strip()

#         if not self.name:
#             raise ValueError("Name is required.")

#         if not self.phone:
#             raise ValueError("Phone number is required.")

#         if not self.contact_id.strip():
#             raise ValueError("Contact ID is required.")

#     def update_details(
#         self,
#         name: str,
#         phone: str,
#         email: str = "",
#     ) -> None:
#         """Update the contact's name, phone, and email."""
#         name = name.strip()
#         phone = phone.strip()
#         email = email.strip()

#         if not name:
#             raise ValueError("Name is required.")

#         if not phone:
#             raise ValueError("Phone number is required.")

#         self.name = name
#         self.phone = phone
#         self.email = email


"""Domain models for the Contact Manager application."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(eq=False)
class Contact:
    """Represent and manage one contact."""

    name: str
    phone: str
    email: str
    contact_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        """Normalize and validate contact data after initialization."""
        self.name = self.name.strip()
        self.phone = self.phone.strip()
        self.email = self.email.strip()
        self.contact_id = self.contact_id.strip()

        if not self.name:
            raise ValueError("Name is required.")

        if not self.phone:
            raise ValueError("Phone number is required.")

        if not self.email:
            raise ValueError("Email is required.")

        if not self.contact_id:
            raise ValueError("Contact ID is required.")

    def update(
        self,
        name: str | None = None,
        phone: str | None = None,
        email: str | None = None,
    ) -> None:
        """Update supplied fields while preserving required-field rules."""
        new_name = self.name if name is None else name.strip()
        new_phone = self.phone if phone is None else phone.strip()
        new_email = self.email if email is None else email.strip()

        if not new_name:
            raise ValueError("Name is required.")

        if not new_phone:
            raise ValueError("Phone number is required.")

        if not new_email:
            raise ValueError("Email is required.")

        self.name = new_name
        self.phone = new_phone
        self.email = new_email

    def __eq__(self, other: object) -> bool:
        """Compare contacts by their stable contact IDs."""
        if not isinstance(other, Contact):
            return NotImplemented
        return self.contact_id == other.contact_id

    def __hash__(self) -> int:
        """Hash a contact using the same ID used for equality."""
        return hash(self.contact_id)
