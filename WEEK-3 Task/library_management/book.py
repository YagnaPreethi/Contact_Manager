"""Book model and book-related operations."""

from dataclasses import asdict, dataclass

from .exceptions import BookNotFoundError
from .validator import validate_positive_integer, validate_required


@dataclass
class Book:
    """Represent a book in the library."""

    book_id: int
    title: str
    author: str
    available: bool = True

    def __post_init__(self) -> None:
        """Validate book information after creation."""
        validate_positive_integer(self.book_id, "Book ID")
        self.title = validate_required(self.title, "Book title")
        self.author = validate_required(self.author, "Author")

    def to_dict(self) -> dict:
        """Convert a book object into a dictionary for JSON storage."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Create a book object from a dictionary."""
        return cls(
            book_id=int(data["book_id"]),
            title=data["title"],
            author=data["author"],
            available=bool(data.get("available", True)),
        )


class BookManager:
    """Manage the library's collection of books."""

    def __init__(self) -> None:
        """Create an empty book collection."""
        self._books: dict[int, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add a book, rejecting duplicate book IDs."""
        if book.book_id in self._books:
            raise ValueError(f"Book ID {book.book_id} already exists.")

        self._books[book.book_id] = book

    def get_book(self, book_id: int) -> Book:
        """Find a book by its ID."""
        if book_id not in self._books:
            raise BookNotFoundError(f"Book ID {book_id} was not found.")

        return self._books[book_id]

    def search_books(self, keyword: str) -> list[Book]:
        """Search book titles and authors without case sensitivity."""
        keyword = keyword.strip().casefold()

        return [
            book
            for book in self._books.values()
            if keyword in book.title.casefold()
            or keyword in book.author.casefold()
        ]

    def update_book(
        self, book_id: int, title: str, author: str
    ) -> Book:
        """Update a book's title and author."""
        book = self.get_book(book_id)
        book.title = validate_required(title, "Book title")
        book.author = validate_required(author, "Author")
        return book

    def delete_book(self, book_id: int) -> Book:
        """Delete a book and return the deleted object."""
        book = self.get_book(book_id)
        del self._books[book_id]
        return book

    def list_books(self) -> list[Book]:
        """Return books in ascending book-ID order."""
        return [
            self._books[book_id]
            for book_id in sorted(self._books)
        ]

    def load_books(self, books: list[Book]) -> None:
        """Load books while checking for duplicate IDs."""
        for book in books:
            self.add_book(book)