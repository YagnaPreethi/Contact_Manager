

"""Tests for Day 3 persistence and data integrity."""

import json
import tempfile
import unittest
from pathlib import Path

from contact_app.models.contact import Contact
from contact_app.persistence.json_contact_repository import (
    JsonContactRepository,
)


class TestJsonContactRepository(unittest.TestCase):
    """Test JSON storage, validation, and recovery."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "contacts.json"
        self.repository = JsonContactRepository(self.path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_missing_file_returns_empty_list(self) -> None:
        self.assertEqual(self.repository.list_all(), [])

    def test_empty_file_raises_clear_error(self) -> None:
        self.path.write_text("", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "empty"):
            self.repository.list_all()

    def test_malformed_json_raises_clear_error(self) -> None:
        self.path.write_text("{invalid json", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            self.repository.list_all()

    def test_unexpected_root_shape_is_rejected(self) -> None:
        self.path.write_text(
            json.dumps({"name": "Priya"}), encoding="utf-8"
        )

        with self.assertRaisesRegex(ValueError, "JSON list"):
            self.repository.list_all()

    def test_invalid_record_is_rejected(self) -> None:
        self.path.write_text(
            json.dumps(["not a contact"]), encoding="utf-8"
        )

        with self.assertRaisesRegex(ValueError, "JSON object"):
            self.repository.list_all()

    def test_duplicate_ids_in_file_are_rejected(self) -> None:
        first = Contact("Priya", "111", contact_id="same-id")
        second = Contact("Ravi", "222", contact_id="same-id")
        self.path.write_text(
            json.dumps([first.to_dict(), second.to_dict()]),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "Duplicate contact ID"):
            self.repository.list_all()

    def test_records_survive_reload(self) -> None:
        original = Contact("Priya", "111", "priya@example.com")
        self.repository.save(original)

        reloaded = JsonContactRepository(self.path)
        found = reloaded.get_by_id(original.contact_id)

        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Priya")
        self.assertEqual(found.contact_id, original.contact_id)

    def test_list_order_is_deterministic(self) -> None:
        second = Contact("Ravi", "222", contact_id="b-id")
        first = Contact("Priya", "111", contact_id="a-id")
        self.repository.save(second)
        self.repository.save(first)

        ids = [contact.contact_id for contact in self.repository.list_all()]
        self.assertEqual(ids, ["a-id", "b-id"])

    def test_old_record_without_id_or_timestamp_loads(self) -> None:
        self.path.write_text(
            json.dumps([
                {"name": "Priya", "phone": "111", "email": ""}
            ]),
            encoding="utf-8",
        )

        contacts = self.repository.list_all()

        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].name, "Priya")
        self.assertTrue(contacts[0].contact_id)

    def test_delete_persists_after_reload(self) -> None:
        contact = Contact("Priya", "111")
        self.repository.save(contact)
        self.repository.delete(contact.contact_id)

        self.assertEqual(
            JsonContactRepository(self.path).list_all(), []
        )


if __name__ == "__main__":
    unittest.main()
