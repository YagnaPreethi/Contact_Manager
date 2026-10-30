"""
Story 3: Magic Methods and Operator Overloading       (28-10-2026)

This program demonstrates:
1. __str__
2. __repr__
3. __len__
4. __eq__
5. __lt__
6. __gt__
7. __add__
8. __sub__
"""


# ============================================================
# 1. __str__ AND __repr__
# ============================================================

class Contact:
    """Represents a contact with a name and phone number."""

    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        # Human-readable description shown by print().
        return f"Contact: {self.name}, Phone: {self.phone}"

    def __repr__(self) -> str:
        # Detailed representation useful for debugging.
        return f"Contact(name={self.name!r}, phone={self.phone!r})"


# ============================================================
# 2. __len__
# ============================================================

class ContactList:
    """Stores contacts and supports len()."""

    def __init__(self, contacts: list[Contact] | None = None) -> None:
        self.contacts = contacts if contacts is not None else []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def __len__(self) -> int:
        # Return the number of contacts in the list.
        return len(self.contacts)


# ============================================================
# 3. __eq__, __lt__, AND __gt__
# ============================================================

class Student:
    """Represents a student whose marks can be compared."""

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented

        return self.marks == other.marks

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented

        return self.marks < other.marks

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented

        return self.marks > other.marks

    def __str__(self) -> str:
        return f"{self.name} ({self.marks} marks)"


# ============================================================
# 4. __add__ AND __sub__
# ============================================================

class Wallet:
    """Represents a wallet containing money."""

    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.balance = balance

    def __add__(self, other: object) -> "Wallet":
        # Adding two wallets creates a new wallet with combined money.
        if not isinstance(other, Wallet):
            return NotImplemented

        return Wallet(self.balance + other.balance)

    def __sub__(self, other: object) -> "Wallet":
        # Subtraction creates a new wallet with the remaining balance.
        if not isinstance(other, Wallet):
            return NotImplemented

        remaining = self.balance - other.balance

        if remaining < 0:
            raise ValueError("Insufficient balance for subtraction.")

        return Wallet(remaining)

    def __str__(self) -> str:
        return f"Wallet balance: ₹{self.balance:.2f}"

    def __repr__(self) -> str:
        return f"Wallet(balance={self.balance!r})"


# ============================================================
# MAIN PROGRAM: DEMONSTRATE ALL MAGIC METHODS
# ============================================================

def main() -> None:
    print("=" * 50)
    print("1. __str__ AND __repr__")
    print("=" * 50)

    contact = Contact("Preethi", "9876543210")

    print("Using str():", str(contact))
    print("Using repr():", repr(contact))

    print("\n" + "=" * 50)
    print("2. __len__")
    print("=" * 50)

    contacts = ContactList()
    contacts.add_contact(Contact("Anjali", "9000000001"))
    contacts.add_contact(Contact("Rahul", "9000000002"))
    contacts.add_contact(Contact("Priya", "9000000003"))

    print("Number of contacts:", len(contacts))

    print("\n" + "=" * 50)
    print("3. __eq__, __lt__, AND __gt__")
    print("=" * 50)

    student1 = Student("Anjali", 85)
    student2 = Student("Rahul", 90)
    student3 = Student("Priya", 85)

    print("Student 1:", student1)
    print("Student 2:", student2)

    print("Student 1 == Student 3:", student1 == student3)
    print("Student 1 < Student 2:", student1 < student2)
    print("Student 2 > Student 1:", student2 > student1)

    print("\n" + "=" * 50)
    print("4. __add__ AND __sub__")
    print("=" * 50)

    wallet1 = Wallet(1000)
    wallet2 = Wallet(500)

    combined_wallet = wallet1 + wallet2
    remaining_wallet = wallet1 - wallet2

    print("Wallet 1:", wallet1)
    print("Wallet 2:", wallet2)
    print("After addition:", combined_wallet)
    print("After subtraction:", remaining_wallet)


if __name__ == "__main__":
    main()