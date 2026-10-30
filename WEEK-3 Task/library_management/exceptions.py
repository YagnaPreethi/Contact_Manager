"""Custom exceptions used by the Library Management System."""


class LibraryError(Exception):
    """Base exception for library-related errors."""


class BookNotFoundError(LibraryError):
    """Raised when a requested book does not exist."""


class MemberNotFoundError(LibraryError):
    """Raised when a requested member does not exist."""


class BookUnavailableError(LibraryError):
    """Raised when a book cannot be issued."""


class ValidationError(LibraryError):
    """Raised when input data is invalid."""