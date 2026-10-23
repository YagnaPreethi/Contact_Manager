
"""Launch the modular Contact Manager."""

from pathlib import Path

from contact_app.cli import run_cli
from contact_app.persistence.json_contact_repository import (
    JsonContactRepository,
)
from contact_app.services.contact_service import ContactService


def main() -> None:
    """Configure the application and start the CLI."""
    data_file = Path(__file__).with_name("contacts.json")
    repository = JsonContactRepository(data_file)
    service = ContactService(repository)
    run_cli(service)


if __name__ == "__main__":
    main()
