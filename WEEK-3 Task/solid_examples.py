"""
Story 5: SOLID Principles
Demonstrating the five SOLID principles using Python.

S - Single Responsibility Principle
O - Open/Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
"""


# ============================================================
# S - SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ============================================================

class Employee:
    """Stores employee information."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class SalaryCalculator:
    """Calculates an employee's annual salary."""

    def calculate_annual_salary(self, employee):
        return employee.salary * 12


def demonstrate_srp():
    print("\n--- Single Responsibility Principle ---")

    employee = Employee("Preethi", 30000)
    calculator = SalaryCalculator()

    annual_salary = calculator.calculate_annual_salary(employee)
    print(f"Employee: {employee.name}")
    print(f"Annual salary: Rs. {annual_salary}")


# Explanation:
# Employee stores employee information.
# SalaryCalculator calculates salary.
# Each class has one main responsibility.


# ============================================================
# O - OPEN/CLOSED PRINCIPLE (OCP)
# ============================================================

from abc import ABC, abstractmethod


class Discount(ABC):
    """Base class for different discount strategies."""

    @abstractmethod
    def calculate(self, price):
        pass


class NoDiscount(Discount):
    def calculate(self, price):
        return price


class TenPercentDiscount(Discount):
    def calculate(self, price):
        return price * 0.90


class ShoppingCart:
    """Calculates the final price using a discount strategy."""

    def __init__(self, discount):
        self.discount = discount

    def final_price(self, price):
        return self.discount.calculate(price)


def demonstrate_ocp():
    print("\n--- Open/Closed Principle ---")

    price = 1000

    regular_cart = ShoppingCart(NoDiscount())
    discounted_cart = ShoppingCart(TenPercentDiscount())

    print(f"Regular price: Rs. {regular_cart.final_price(price):.2f}")
    print(f"Discounted price: Rs. {discounted_cart.final_price(price):.2f}")


# Explanation:
# New discount types can be added by creating new Discount subclasses.
# ShoppingCart does not need to be rewritten for every new discount.


# ============================================================
# L - LISKOV SUBSTITUTION PRINCIPLE (LSP)
# ============================================================

class Bird(ABC):
    """Base class for birds."""

    @abstractmethod
    def eat(self):
        pass


class Sparrow(Bird):
    def eat(self):
        return "Sparrow is eating."


class Penguin(Bird):
    def eat(self):
        return "Penguin is eating."


def make_bird_eat(bird):
    print(bird.eat())


def demonstrate_lsp():
    print("\n--- Liskov Substitution Principle ---")

    birds = [Sparrow(), Penguin()]

    for bird in birds:
        make_bird_eat(bird)


# Explanation:
# Sparrow and Penguin both follow the Bird contract.
# Either object can be passed to make_bird_eat() without breaking it.
# The base class only requires eating, so flight behavior is not assumed.


# ============================================================
# I - INTERFACE SEGREGATION PRINCIPLE (ISP)
# ============================================================

class Printer(ABC):
    """Interface for printing."""

    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    """Interface for scanning."""

    @abstractmethod
    def scan_document(self):
        pass


class SimplePrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"


class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self):
        return "Scanning document."


def demonstrate_isp():
    print("\n--- Interface Segregation Principle ---")

    simple_printer = SimplePrinter()
    multi_printer = MultiFunctionPrinter()

    print(simple_printer.print_document("Python Notes"))
    print(multi_printer.print_document("SOLID Principles"))
    print(multi_printer.scan_document())


# Explanation:
# Printing and scanning are separate interfaces.
# SimplePrinter only implements printing.
# It is not forced to implement a scanning method it does not support.


# ============================================================
# D - DEPENDENCY INVERSION PRINCIPLE (DIP)
# ============================================================

class NotificationService(ABC):
    """Abstraction for sending notifications."""

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotification(NotificationService):
    def send(self, message):
        return f"SMS sent: {message}"


class OrderService:
    """Sends order notifications using an injected service."""

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def place_order(self):
        return self.notification_service.send("Your order has been placed.")


def demonstrate_dip():
    print("\n--- Dependency Inversion Principle ---")

    email_service = EmailNotification()
    email_order = OrderService(email_service)
    print(email_order.place_order())

    sms_service = SMSNotification()
    sms_order = OrderService(sms_service)
    print(sms_order.place_order())


# Explanation:
# OrderService depends on the NotificationService abstraction.
# EmailNotification and SMSNotification are interchangeable implementations.
# A new notification method can be added without rewriting OrderService.


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    demonstrate_srp()
    demonstrate_ocp()
    demonstrate_lsp()
    demonstrate_isp()
    demonstrate_dip()


if __name__ == "__main__":
    main()