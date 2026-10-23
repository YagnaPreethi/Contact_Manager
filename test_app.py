
import tempfile
import unittest
from pathlib import Path

from app import (
    add_contact,
    delete_contact,
    load_contacts,
    save_contacts,
    search_contacts,
    update_contact,
)


class TestContactManager(unittest.TestCase):

    def setUp(self):
        self.contacts = []
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "contacts.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_contact(self):
        add_contact(
            self.contacts, "Priya", "9876543210", "priya@gmail.com"
        )

        self.assertEqual(len(self.contacts), 1)
        self.assertEqual(self.contacts[0]["name"], "Priya")

    def test_duplicate_phone_is_rejected(self):
        add_contact(self.contacts, "Priya", "9876543210", "p@gmail.com")

        with self.assertRaises(ValueError):
            add_contact(self.contacts, "Rahul", "9876543210", "r@gmail.com")

    def test_search_contact(self):
        add_contact(self.contacts, "Priya", "9876543210", "p@gmail.com")

        results = search_contacts(self.contacts, "priya")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Priya")

    def test_update_contact(self):
        add_contact(self.contacts, "Priya", "9876543210", "p@gmail.com")

        result = update_contact(
            self.contacts,
            "9876543210",
            "Priya Sharma",
            "9999999999",
            "new@gmail.com",
        )

        self.assertTrue(result)
        self.assertEqual(self.contacts[0]["name"], "Priya Sharma")
        self.assertEqual(self.contacts[0]["phone"], "9999999999")

    def test_delete_contact(self):
        add_contact(self.contacts, "Priya", "9876543210", "p@gmail.com")

        result = delete_contact(self.contacts, "9876543210")

        self.assertTrue(result)
        self.assertEqual(len(self.contacts), 0)

    def test_save_and_load_contacts(self):
        add_contact(self.contacts, "Priya", "9876543210", "p@gmail.com")

        save_contacts(self.contacts, self.file_path)
        loaded_contacts = load_contacts(self.file_path)

        self.assertEqual(loaded_contacts, self.contacts)

    def test_missing_file_returns_empty_list(self):
        loaded_contacts = load_contacts(self.file_path)

        self.assertEqual(loaded_contacts, [])


if __name__ == "__main__":
    unittest.main()
