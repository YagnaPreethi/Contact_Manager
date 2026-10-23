# """Tests for the Contact domain model."""

# import unittest
# from contact import Contact


# class TestContact(unittest.TestCase):

#     def test_create_contact(self):
#         contact = Contact(
#             name="Priya",
#             phone="9876543210",
#             email="priya@example.com",
#         )

#         self.assertEqual(contact.name, "Priya")
#         self.assertEqual(contact.phone, "9876543210")
#         self.assertEqual(contact.email, "priya@example.com")
#         self.assertTrue(contact.contact_id)
#         self.assertIsNotNone(contact.created_at)

#     def test_name_is_required(self):
#         with self.assertRaises(ValueError):
#             Contact(name="  ", phone="9876543210")

#     def test_phone_is_required(self):
#         with self.assertRaises(ValueError):
#             Contact(name="Priya", phone="  ")

#     def test_update_contact(self):
#         contact = Contact(name="Priya", phone="9876543210")

#         contact.update_details(
#             name="Priya Sharma",
#             phone="9876501234",
#             email="priya@example.com",
#         )

#         self.assertEqual(contact.name, "Priya Sharma")
#         self.assertEqual(contact.phone, "9876501234")
#         self.assertEqual(contact.email, "priya@example.com")

#     def test_each_contact_has_unique_id(self):
#         first = Contact(name="Priya", phone="1111111111")
#         second = Contact(name="Ravi", phone="2222222222")

#         self.assertNotEqual(first.contact_id, second.contact_id)


# if __name__ == "__main__":
#     unittest.main()


"""Tests for the Contact domain model."""

import unittest
from datetime import datetime, timezone

from domain_models import Contact


class TestContact(unittest.TestCase):
    """Test Contact creation, validation, and behaviour."""

    def test_contact_creation(self) -> None:
        contact = Contact("Kedari", "9642342743", "kedari@gmail.com")

        self.assertEqual(contact.name, "Kedari")
        self.assertTrue(contact.contact_id)
        self.assertIsInstance(contact.created_at, datetime)
        self.assertIsNotNone(contact.created_at.tzinfo)

    def test_required_name(self) -> None:
        with self.assertRaises(ValueError):
            Contact("", "9642342743", "kedari@gmail.com")

    def test_required_phone(self) -> None:
        with self.assertRaises(ValueError):
            Contact("Kedari", " ", "kedari@gmail.com")

    def test_required_email(self) -> None:
        with self.assertRaises(ValueError):
            Contact("Kedari", "9642342743", "")

    def test_update_contact(self) -> None:
        contact = Contact("Kedari", "9642342743", "kedari@gmail.com")
        contact.update(phone="9123456780")

        self.assertEqual(contact.phone, "9123456780")
        self.assertEqual(contact.name, "Kedari")

    def test_invalid_update_does_not_change_contact(self) -> None:
        contact = Contact("Kedari", "9642342743", "kedari@gmail.com")

        with self.assertRaises(ValueError):
            contact.update(name=" ")

        self.assertEqual(contact.name, "Kedari")

    def test_contacts_compare_by_id(self) -> None:
        first = Contact(
            "Kedari", "1111111111", "first@example.com",
            contact_id="contact-123",
        )
        second = Contact(
            "Another Name", "2222222222", "second@example.com",
            contact_id="contact-123",
        )

        self.assertEqual(first, second)
        self.assertEqual(hash(first), hash(second))

    def test_created_at_is_utc(self) -> None:
        contact = Contact("Kedari", "9642342743", "kedari@gmail.com")

        self.assertEqual(contact.created_at.utcoffset().total_seconds(), 0)


if __name__ == "__main__":
    unittest.main()
