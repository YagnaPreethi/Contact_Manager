"""
Week 3 - Story 2: OOP Implementation in Python   (27-10-2026)

Concepts demonstrated:
1. Encapsulation
2. Single inheritance
3. Multiple inheritance
4. Multilevel inheritance
5. Hierarchical inheritance
6. Polymorphism and method overriding
7. Method overloading using default arguments
8. Composition
9. Aggregation

Run:
python oop_examples.py
"""


# ============================================================
# 1. ENCAPSULATION
# ============================================================
# Encapsulation combines data and methods inside a class.
# The double underscore makes direct access to this attribute
# harder through Python's name-mangling mechanism.
# Public methods provide controlled access to the balance.


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        self.__balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    def get_balance(self) -> float:
        return self.__balance


def demonstrate_encapsulation() -> None:
    print("\n--- 1. Encapsulation ---")

    account = BankAccount("Anu", 1000)
    account.deposit(500)

    print("Account holder:", account.owner)
    print("Current balance:", account.get_balance())


# ============================================================
# 2. SINGLE INHERITANCE
# ============================================================
# A child class inherits from one parent class.
# Employee inherits the name and introduce() method from Person.


class Person:
    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> None:
        print(f"My name is {self.name}.")


class Employee(Person):
    def __init__(self, name: str, employee_id: str):
        super().__init__(name)
        self.employee_id = employee_id

    def show_employee_id(self) -> None:
        print(f"Employee ID: {self.employee_id}")


def demonstrate_single_inheritance() -> None:
    print("\n--- 2. Single Inheritance ---")

    employee = Employee("Ravi", "EMP101")
    employee.introduce()
    employee.show_employee_id()


# ============================================================
# 3. MULTIPLE INHERITANCE
# ============================================================
# A child class inherits from two or more parent classes.
# Smartphone receives methods from both Camera and Phone.


class Camera:
    def take_photo(self) -> None:
        print("Photo captured.")


class Phone:
    def make_call(self) -> None:
        print("Making a phone call.")


class Smartphone(Camera, Phone):
    pass


def demonstrate_multiple_inheritance() -> None:
    print("\n--- 3. Multiple Inheritance ---")

    mobile = Smartphone()
    mobile.take_photo()
    mobile.make_call()


# ============================================================
# 4. MULTILEVEL INHERITANCE
# ============================================================
# Inheritance forms a chain:
# Person -> Employee -> Manager.
# Manager inherits methods from both Employee and Person.


class Manager(Employee):
    def conduct_meeting(self) -> None:
        print(f"{self.name} is conducting a meeting.")


def demonstrate_multilevel_inheritance() -> None:
    print("\n--- 4. Multilevel Inheritance ---")

    manager = Manager("Priya", "EMP202")
    manager.introduce()
    manager.show_employee_id()
    manager.conduct_meeting()


# ============================================================
# 5. HIERARCHICAL INHERITANCE
# ============================================================
# Multiple child classes inherit from the same parent class.
# Developer and Designer both inherit from Person.


class Developer(Person):
    def write_code(self) -> None:
        print(f"{self.name} is writing Python code.")


class Designer(Person):
    def design_interface(self) -> None:
        print(f"{self.name} is designing an interface.")


def demonstrate_hierarchical_inheritance() -> None:
    print("\n--- 5. Hierarchical Inheritance ---")

    developer = Developer("Arun")
    designer = Designer("Meena")

    developer.introduce()
    developer.write_code()

    designer.introduce()
    designer.design_interface()


# ============================================================
# 6. POLYMORPHISM AND METHOD OVERRIDING
# ============================================================
# Polymorphism allows different objects to respond to the
# same method call in different ways.
#
# EmailNotification and SMSNotification override the send()
# method inherited from Notification.


class Notification:
    def send(self) -> None:
        print("Sending a general notification.")


class EmailNotification(Notification):
    def send(self) -> None:
        print("Sending an email notification.")


class SMSNotification(Notification):
    def send(self) -> None:
        print("Sending an SMS notification.")


def demonstrate_polymorphism() -> None:
    print("\n--- 6. Polymorphism and Method Overriding ---")

    notifications = [
        Notification(),
        EmailNotification(),
        SMSNotification(),
    ]

    # The same method call produces different results.
    for notification in notifications:
        notification.send()


# ============================================================
# 7. METHOD OVERLOADING USING DEFAULT ARGUMENTS
# ============================================================
# Python does not provide traditional signature-based method
# overloading in the same way as some other languages.
# Default arguments allow one method to handle different
# numbers of supplied arguments.


class Calculator:
    def add(self, a: int, b: int = 0, c: int = 0) -> int:
        return a + b + c


def demonstrate_method_overloading() -> None:
    print("\n--- 7. Method Overloading Using Default Arguments ---")

    calculator = Calculator()

    print("One number:", calculator.add(10))
    print("Two numbers:", calculator.add(10, 20))
    print("Three numbers:", calculator.add(10, 20, 30))


# ============================================================
# 8. COMPOSITION
# ============================================================
# Composition models a strong whole-part relationship.
# In this example, Car creates and stores its own Engine.
# The Engine is used as a component of the Car.


class Engine:
    def start(self) -> None:
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self) -> None:
        self.engine.start()
        print("Car is ready to drive.")


def demonstrate_composition() -> None:
    print("\n--- 8. Composition ---")

    car = Car()
    car.start_car()


# ============================================================
# 9. AGGREGATION
# ============================================================
# Aggregation models a relationship in which one object
# references another object that can exist independently.
#
# Person is created separately and then passed to Department.


class Department:
    def __init__(self, name: str, employee: Person):
        self.name = name
        self.employee = employee

    def show_details(self) -> None:
        print(f"Department: {self.name}")
        print(f"Employee: {self.employee.name}")


def demonstrate_aggregation() -> None:
    print("\n--- 9. Aggregation ---")

    employee = Person("Kiran")
    department = Department("IT", employee)

    department.show_details()

    # The employee object still has an independent reference.
    print("Employee exists independently:", employee.name)


# ============================================================
# MAIN PROGRAM
# ============================================================
# Run each demonstration in sequence when this file is
# executed directly.


def main() -> None:
    demonstrate_encapsulation()
    demonstrate_single_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_multilevel_inheritance()
    demonstrate_hierarchical_inheritance()
    demonstrate_polymorphism()
    demonstrate_method_overloading()
    demonstrate_composition()
    demonstrate_aggregation()


if __name__ == "__main__":
    main()