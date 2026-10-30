"""Member model and member-related operations."""

from dataclasses import asdict, dataclass

from .exceptions import MemberNotFoundError
from .validator import validate_positive_integer, validate_required


@dataclass
class Member:
    """Represent a registered library member."""

    member_id: int
    name: str
    email: str
    active: bool = True

    def __post_init__(self) -> None:
        """Validate member information."""
        validate_positive_integer(self.member_id, "Member ID")
        self.name = validate_required(self.name, "Member name")
        self.email = validate_required(self.email, "Email")

        if "@" not in self.email:
            raise ValueError("Please provide a valid email address.")

    def to_dict(self) -> dict:
        """Convert a member into a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        """Create a member from a dictionary."""
        return cls(
            member_id=int(data["member_id"]),
            name=data["name"],
            email=data["email"],
            active=bool(data.get("active", True)),
        )


class MemberManager:
    """Manage registered library members."""

    def __init__(self) -> None:
        """Create an empty member collection."""
        self._members: dict[int, Member] = {}

    def register_member(self, member: Member) -> None:
        """Register a new member."""
        if member.member_id in self._members:
            raise ValueError(
                f"Member ID {member.member_id} already exists."
            )

        self._members[member.member_id] = member

    def get_member(self, member_id: int) -> Member:
        """Find a member by ID and ensure membership is active."""
        if member_id not in self._members:
            raise MemberNotFoundError(
                f"Member ID {member_id} was not found."
            )

        member = self._members[member_id]

        if not member.active:
            raise ValueError("This member is inactive.")

        return member

    def update_member(
        self, member_id: int, name: str, email: str
    ) -> Member:
        """Update a registered member's information."""
        member = self.get_member(member_id)
        member.name = validate_required(name, "Member name")
        member.email = validate_required(email, "Email")

        if "@" not in member.email:
            raise ValueError("Please provide a valid email address.")

        return member

    def delete_member(self, member_id: int) -> Member:
        """Remove a member from the collection."""
        member = self.get_member(member_id)
        del self._members[member_id]
        return member

    def list_members(self) -> list[Member]:
        """Return all members in ascending ID order."""
        return [
            self._members[member_id]
            for member_id in sorted(self._members)
        ]

    def load_members(self, members: list[Member]) -> None:
        """Load members while checking for duplicate IDs."""
        for member in members:
            self.register_member(member)