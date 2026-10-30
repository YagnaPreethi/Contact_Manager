"""Command-line application for the Library Management System."""

from .book import Book, BookManager
from .exceptions import LibraryError
from .issue import IssueManager, IssueRecord
from .member import Member, MemberManager
from .reports import LibraryReports
from .storage import load_json, save_json


def build_library():
    """Load stored data and create the library services."""
    books = BookManager()
    members = MemberManager()

    books.load_books([
        Book.from_dict(item)
        for item in load_json("books.json")
    ])

    members.load_members([
        Member.from_dict(item)
        for item in load_json("members.json")
    ])

    issues = IssueManager(books, members)
    issues.load_issues([
        IssueRecord.from_dict(item)
        for item in load_json("issues.json")
    ])

    # Restore availability from the active issue records.
    for record in issues.list_issues():
        if record.return_date is None:
            books.get_book(record.book_id).available = False

    reports = LibraryReports(books, members, issues)

    return books, members, issues, reports


def save_library(books, members, issues) -> None:
    """Save all library records to JSON files."""
    save_json(
        "books.json",
        [book.to_dict() for book in books.list_books()],
    )
    save_json(
        "members.json",
        [member.to_dict() for member in members.list_members()],
    )
    save_json(
        "issues.json",
        [record.to_dict() for record in issues.list_issues()],
    )


def main() -> None:
    """Run the library menu."""
    try:
        books, members, issues, reports = build_library()
    except (ValueError, KeyError, TypeError, LibraryError) as exc:
        print(f"Could not load library data: {exc}")
        return

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add book")
        print("2. List books")
        print("3. Search books")
        print("4. Update book")
        print("5. Delete book")
        print("6. Register member")
        print("7. List members")
        print("8. Issue book")
        print("9. Return book")
        print("10. Library reports")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                book_id = int(input("Book ID: "))
                title = input("Book title: ")
                author = input("Author: ")
                books.add_book(Book(book_id, title, author))
                save_library(books, members, issues)
                print("Book added successfully.")

            elif choice == "2":
                for book in books.list_books():
                    status = "Available" if book.available else "Borrowed"
                    print(
                        f"{book.book_id}: {book.title} "
                        f"by {book.author} - {status}"
                    )

            elif choice == "3":
                keyword = input("Enter title or author keyword: ")
                matches = books.search_books(keyword)

                if not matches:
                    print("No matching books found.")

                for book in matches:
                    print(f"{book.book_id}: {book.title} by {book.author}")

            elif choice == "4":
                book_id = int(input("Book ID to update: "))
                title = input("New title: ")
                author = input("New author: ")
                books.update_book(book_id, title, author)
                save_library(books, members, issues)
                print("Book updated successfully.")

            elif choice == "5":
                book_id = int(input("Book ID to delete: "))
                book = books.get_book(book_id)

                if not book.available:
                    print("Return the borrowed book before deleting it.")
                    continue

                books.delete_book(book_id)
                save_library(books, members, issues)
                print("Book deleted successfully.")

            elif choice == "6":
                member_id = int(input("Member ID: "))
                name = input("Member name: ")
                email = input("Email: ")
                members.register_member(Member(member_id, name, email))
                save_library(books, members, issues)
                print("Member registered successfully.")

            elif choice == "7":
                for member in members.list_members():
                    print(
                        f"{member.member_id}: {member.name} "
                        f"({member.email}) - "
                        f"{'Active' if member.active else 'Inactive'}"
                    )

            elif choice == "8":
                book_id = int(input("Book ID to issue: "))
                member_id = int(input("Member ID: "))
                record = issues.issue_book(book_id, member_id)
                save_library(books, members, issues)
                print(
                    f"Book issued. Issue ID: {record.issue_id}; "
                    f"due date: {record.due_date}"
                )

            elif choice == "9":
                issue_id = int(input("Issue ID to return: "))
                record = issues.return_book(issue_id)
                save_library(books, members, issues)
                print(
                    f"Book returned. Fine: ₹{record.fine:.2f}"
                )

            elif choice == "10":
                print("\nAvailable books:")
                for book in reports.available_books():
                    print(f"{book.book_id}: {book.title}")

                print("\nBorrowed books:")
                for book in reports.borrowed_books():
                    print(f"{book.book_id}: {book.title}")

                print("\nTop borrowers (member ID, borrow count):")
                print(reports.top_borrowers())

                print("\nFine report (issue ID, fine):")
                print(reports.fine_report())

            elif choice == "0":
                save_library(books, members, issues)
                print("Library data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a menu option.")

        except (ValueError, LibraryError, KeyError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()