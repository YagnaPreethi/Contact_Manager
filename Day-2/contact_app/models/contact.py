
"""Contact domain model."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class Contact:
    """Represent a single contact."""

    name: str
    phone: str
    email: str = ""
    contact_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        """Normalize and validate contact details."""
        self.name = self.name.strip()
        self.phone = self.phone.strip()
        self.email = self.email.strip()

        if not self.name:
            raise ValueError("Name is required.")
        if not self.phone:
            raise ValueError("Phone number is required.")

    def update_details(
        self,
        name: str | None = None,
        phone: str | None = None,
        email: str | None = None,
    ) -> None:
        """Update supplied details after validating them."""
        new_name = self.name if name is None else name.strip()
        new_phone = self.phone if phone is None else phone.strip()
        new_email = self.email if email is None else email.strip()

        if not new_name:
            raise ValueError("Name is required.")
        if not new_phone:
            raise ValueError("Phone number is required.")

        self.name = new_name
        self.phone = new_phone
        self.email = new_email

    def to_dict(self) -> dict[str, str]:
        """Convert the contact into JSON-compatible values."""
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Contact":
        """Create a Contact from stored dictionary data."""
        timestamp = data.get("created_at")

        return cls(
            name=data["name"],
            phone=data["phone"],
            email=data.get("email", ""),
            contact_id=data.get("contact_id") or str(uuid4()),
            created_at=(
                datetime.fromisoformat(timestamp)
                if timestamp
                else datetime.now(timezone.utc)
            ),
        )
