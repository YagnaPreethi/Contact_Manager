"""Validation functions for library data."""

from .exceptions import ValidationError


def validate_required(value: str, field_name: str) -> str:
    """Return a cleaned string or raise an error if it is empty."""
    cleaned_value = value.strip()

    if not cleaned_value:
        raise ValidationError(f"{field_name} cannot be empty.")

    return cleaned_value


def validate_positive_integer(value: int, field_name: str) -> int:
    """Ensure an integer value is greater than zero."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValidationError(f"{field_name} must be a positive integer.")

    return value