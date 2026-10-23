
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts(file_path=DATA_FILE):
    """Load contacts from a JSON file."""
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            contacts = json.load(file)

        if not isinstance(contacts, list):
            raise ValueError("Contact data must be a list.")

        return contacts

    except json.JSONDecodeError as error:
        raise ValueError("The contacts file contains invalid JSON.") from error


def save_contacts(contacts, file_path=DATA_FILE):
    """Save contacts to a JSON file."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts, name, phone, email):
    """Add a new contact."""
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    if not name or not phone:
        raise ValueError("Name and phone are required.")

    if any(contact["phone"] == phone for contact in contacts):
        raise ValueError("This phone number already exists.")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    return contact


def search_contacts(contacts, keyword):
    """Search contacts by name, phone, or email."""
    keyword = keyword.strip().lower()

    return [
        contact for contact in contacts
        if keyword in contact["name"].lower()
        or keyword in contact["phone"].lower()
        or keyword in contact["email"].lower()
    ]


def update_contact(contacts, phone, new_name, new_phone, new_email):
    """Update an existing contact using its current phone number."""
    for contact in contacts:
        if contact["phone"] == phone:
            new_name = new_name.strip()
            new_phone = new_phone.strip()
            new_email = new_email.strip()

            if not new_name or not new_phone:
                raise ValueError("Name and phone are required.")

            if any(
                item["phone"] == new_phone and item is not contact
                for item in contacts
            ):
                raise ValueError("This phone number already exists.")

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            return True

    return False


def delete_contact(contacts, phone):
    """Delete a contact using its phone number."""
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            return True

    return False


def display_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found.")
        return

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGER =====")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")

                add_contact(contacts, name, phone, email)
                save_contacts(contacts)
                print("Contact added successfully!")

            elif choice == "2":
                display_contacts(contacts)
            # elif choice == "2":
            #     print("DEBUG: Option 2 selected")
            #     print("DEBUG: Contacts loaded =", repr(contacts))
            #     display_contacts(contacts)
            #     print("DEBUG: Display function completed")


            elif choice == "3":
                keyword = input("Enter name, phone, or email: ")
                results = search_contacts(contacts, keyword)
                display_contacts(results)

            elif choice == "4":
                phone = input("Enter current phone number: ")
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")

                if update_contact(
                    contacts, phone, new_name, new_phone, new_email
                ):
                    save_contacts(contacts)
                    print("Contact updated successfully!")
                else:
                    print("Contact not found.")

            elif choice == "5":
                phone = input("Enter phone number to delete: ")

                if delete_contact(contacts, phone):
                    save_contacts(contacts)
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found.")

            elif choice == "6":
                print("Thank you for using Contact Manager!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
