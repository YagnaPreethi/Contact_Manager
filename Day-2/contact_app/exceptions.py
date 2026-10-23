
"""Application-specific exceptions."""


class ContactManagerError(Exception):
    """Base exception for Contact Manager errors."""


class ContactNotFoundError(ContactManagerError):
    """Raised when a requested contact does not exist."""


class DuplicateContactError(ContactManagerError):
    """Raised when a phone number is already registered."""


class InvalidContactError(ContactManagerError):
    """Raised when contact data is invalid."""


class UnsupportedOperationError(ContactManagerError):
    """Raised when an operation is not supported."""
