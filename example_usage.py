
"""Example demonstrating how to use the Contact model."""

from domain_models import Contact


def main() -> None:
    """Create, display, and update a contact."""
    contact = Contact(
        name="Kedari",
        phone="9642342743",
        email="kedari@gmail.com",
    )

    print("Contact created successfully!")
    print(f"ID: {contact.contact_id}")
    print(f"Name: {contact.name}")
    print(f"Phone: {contact.phone}")
    print(f"Email: {contact.email}")
    print(f"Created at: {contact.created_at.isoformat()}")

    contact.update(phone="9123456780")

    print("\nAfter updating:")
    print(f"Phone: {contact.phone}")


if __name__ == "__main__":
    main()
