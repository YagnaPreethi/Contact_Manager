
"""Tests for the Day 2 contact service."""

import tempfile
import unittest
from pathlib import Path

from contact_app.exceptions import (
    ContactNotFoundError,
    DuplicateContactError,
    InvalidContactError,
)
from contact_app.persistence.json_contact_repository import (
    JsonContactRepository,
)
from contact_app.services.contact_service import ContactService


class TestContactService(unittest.TestCase):
    """Test contact CRUD operations without the CLI."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        path = Path(self.temp_dir.name) / "contacts.json"
        self.repository = JsonContactRepository(path)
        self.service = ContactService(self.repository)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_create_and_retrieve(self) -> None:
        created = self.service.create_contact(
            "Priya", "9876543210", "priya@example.com"
        )
        found = self.service.get_contact(created.contact_id)

        self.assertEqual(found.name, "Priya")
        self.assertEqual(found.phone, "9876543210")

    def test_list_contacts(self) -> None:
        self.service.create_contact("Priya", "111", "priya@example.com")
        self.service.create_contact("Ravi", "222", "ravi@example.com")

        self.assertEqual(len(self.service.list_contacts()), 2)

    def test_update_contact(self) -> None:
        contact = self.service.create_contact("Priya", "111")
        updated = self.service.update_contact(
            contact.contact_id, name="Priya K", phone="333"
        )

        self.assertEqual(updated.name, "Priya K")
        self.assertEqual(updated.phone, "333")

    def test_delete_contact(self) -> None:
        contact = self.service.create_contact("Priya", "111")
        self.service.delete_contact(contact.contact_id)

        self.assertEqual(self.service.list_contacts(), [])

    def test_missing_contact_raises_error(self) -> None:
        with self.assertRaises(ContactNotFoundError):
            self.service.get_contact("does-not-exist")

    def test_duplicate_phone_raises_error(self) -> None:
        self.service.create_contact("Priya", "111")

        with self.assertRaises(DuplicateContactError):
            self.service.create_contact("Ravi", "111")

    def test_blank_name_raises_error(self) -> None:
        with self.assertRaises(InvalidContactError):
            self.service.create_contact(" ", "111")

    def test_blank_phone_raises_error(self) -> None:
        with self.assertRaises(InvalidContactError):
            self.service.create_contact("Priya", " ")

    def test_updated_duplicate_phone_is_rejected(self) -> None:
        first = self.service.create_contact("Priya", "111")
        second = self.service.create_contact("Ravi", "222")

        with self.assertRaises(DuplicateContactError):
            self.service.update_contact(second.contact_id, phone="111")

        # The rejected update must not change the stored contact.
        unchanged = self.service.get_contact(second.contact_id)
        self.assertEqual(unchanged.phone, "222")


if __name__ == "__main__":
    unittest.main()
