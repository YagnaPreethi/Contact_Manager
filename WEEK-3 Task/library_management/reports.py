"""Reporting functions for the library application."""

from .book import BookManager
from .issue import IssueManager
from .member import MemberManager


class LibraryReports:
    """Generate reports from library managers."""

    def __init__(
        self,
        books: BookManager,
        members: MemberManager,
        issues: IssueManager,
    ) -> None:
        """Receive the managers required for reporting."""
        self.books = books
        self.members = members
        self.issues = issues

    def available_books(self) -> list:
        """Return all currently available books."""
        return [
            book
            for book in self.books.list_books()
            if book.available
        ]

    def borrowed_books(self) -> list:
        """Return all currently borrowed books."""
        return [
            book
            for book in self.books.list_books()
            if not book.available
        ]

    def top_borrowers(self, limit: int = 5) -> list[tuple[int, int]]:
        """Return member IDs and their borrowing counts."""
        counts: dict[int, int] = {}

        for record in self.issues.list_issues():
            counts[record.member_id] = (
                counts.get(record.member_id, 0) + 1
            )

        return sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0]),
        )[:limit]

    def fine_report(self) -> list[tuple[int, float]]:
        """Return issue IDs and any fines charged."""
        return [
            (record.issue_id, record.fine)
            for record in self.issues.list_issues()
            if record.fine > 0
        ]