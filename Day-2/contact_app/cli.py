
"""Command-line interface for Contact Manager."""

from contact_app.exceptions import ContactManagerError
from contact_app.services.contact_service import ContactService


def display_contacts(service: ContactService) -> None:
    """Print all stored contacts."""
    contacts = service.list_contacts()

    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        print(f"\nID:    {contact.contact_id}")
        print(f"Name:  {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")


def run_cli(service: ContactService) -> None:
    """Run the menu using an already configured service."""
    while True:
        print("\n===== CONTACT MANAGER =====")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Retrieve contact by ID")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                contact = service.create_contact(
                    input("Enter name: "),
                    input("Enter phone: "),
                    input("Enter email (optional): "),
                )
                print(f"Contact created. ID: {contact.contact_id}")

            elif choice == "2":
                display_contacts(service)

            elif choice == "3":
                contact = service.get_contact(
                    input("Enter contact ID: ").strip()
                )
                print(
                    f"{contact.name} | {contact.phone} | {contact.email}"
                )

            elif choice == "4":
                contact_id = input("Enter contact ID: ").strip()
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")

                contact = service.update_contact(
                    contact_id, name, phone, email
                )
                print(f"Updated contact: {contact.name}")

            elif choice == "5":
                contact_id = input("Enter contact ID: ").strip()
                service.delete_contact(contact_id)
                print("Contact deleted successfully.")

            elif choice == "6":
                print("Thank you for using Contact Manager!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")

        except (ContactManagerError, ValueError) as error:
            print(f"Error: {error}")
