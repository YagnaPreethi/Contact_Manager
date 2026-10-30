"""Book issue, return, and fine calculations."""

from dataclasses import asdict, dataclass
from datetime import date, timedelta

from .book import BookManager
from .exceptions import BookUnavailableError
from .member import MemberManager
from .validator import validate_positive_integer


@dataclass
class IssueRecord:
    """Represent a book issue transaction."""

    issue_id: int
    book_id: int
    member_id: int
    issue_date: str
    due_date: str
    return_date: str | None = None
    fine: float = 0.0

    def to_dict(self) -> dict:
        """Convert an issue record to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "IssueRecord":
        """Create an issue record from a dictionary."""
        return cls(**data)


class IssueManager:
    """Coordinate book issues and returns."""

    FINE_PER_DAY = 5.0

    def __init__(
        self,
        books: BookManager,
        members: MemberManager,
        loan_days: int = 14,
    ) -> None:
        """Receive the managers needed for issue operations."""
        validate_positive_integer(loan_days, "Loan period")
        self.books = books
        self.members = members
        self.loan_days = loan_days
        self._records: dict[int, IssueRecord] = {}
        self._next_issue_id = 1

    def issue_book(
        self,
        book_id: int,
        member_id: int,
        issue_date: date | None = None,
    ) -> IssueRecord:
        """Issue an available book to an active member."""
        book = self.books.get_book(book_id)
        self.members.get_member(member_id)

        if not book.available:
            raise BookUnavailableError(
                f"Book ID {book_id} is already borrowed."
            )

        today = issue_date or date.today()
        record = IssueRecord(
            issue_id=self._next_issue_id,
            book_id=book_id,
            member_id=member_id,
            issue_date=today.isoformat(),
            due_date=(today + timedelta(days=self.loan_days)).isoformat(),
        )

        self._records[record.issue_id] = record
        self._next_issue_id += 1
        book.available = False

        return record

    def return_book(
        self,
        issue_id: int,
        return_date: date | None = None,
    ) -> IssueRecord:
        """Return a borrowed book and calculate any late fine."""
        if issue_id not in self._records:
            raise ValueError(f"Issue ID {issue_id} was not found.")

        record = self._records[issue_id]

        if record.return_date is not None:
            raise ValueError("This issue has already been returned.")

        returned_on = return_date or date.today()
        due_on = date.fromisoformat(record.due_date)
        late_days = max((returned_on - due_on).days, 0)

        record.return_date = returned_on.isoformat()
        record.fine = late_days * self.FINE_PER_DAY

        self.books.get_book(record.book_id).available = True

        return record

    def list_issues(self) -> list[IssueRecord]:
        """Return issue records in issue-ID order."""
        return [
            self._records[key]
            for key in sorted(self._records)
        ]

    def load_issues(self, records: list[IssueRecord]) -> None:
        """Load issue records and determine the next issue ID."""
        for record in records:
            if record.issue_id in self._records:
                raise ValueError(
                    f"Issue ID {record.issue_id} already exists."
                )

            self._records[record.issue_id] = record

        if self._records:
            self._next_issue_id = max(self._records) + 1