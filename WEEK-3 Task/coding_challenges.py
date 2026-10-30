"""
Story 6 - OOP Coding Challenges

1. Student class
2. Bank account class
3. Employee management
4. Vehicle inheritance
5. Shape area calculator
6. Shopping cart
7. Movie rating system
8. Hospital patient records
9. School result processing
10. Online course management
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. STUDENT CLASS
# ============================================================

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 35


def challenge_1():
    print("\n=== 1. Student Class ===")

    student = Student("Preethi", 101, 85)
    student.display_details()

    if student.has_passed():
        print("Result: Pass")
    else:
        print("Result: Fail")


# ============================================================
# 2. BANK ACCOUNT CLASS
# ============================================================

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: Rs. {self.__balance:.2f}")


def challenge_2():
    print("\n=== 2. Bank Account ===")

    account = BankAccount("Preethi", 5000)
    account.deposit(1000)
    account.withdraw(1500)
    account.display_balance()


# ============================================================
# 3. EMPLOYEE MANAGEMENT
# ============================================================

class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department} | "
            f"Salary: Rs. {self.salary:.2f}"
        )


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if self.find_employee(employee.employee_id):
            print("Employee ID already exists.")
            return

        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def display_all(self):
        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.display()


def challenge_3():
    print("\n=== 3. Employee Management ===")

    manager = EmployeeManager()

    manager.add_employee(
        Employee(1, "Preethi", "IT", 35000)
    )
    manager.add_employee(
        Employee(2, "Rahul", "HR", 30000)
    )

    print("\nEmployee records:")
    manager.display_all()

    print("\nSearching for employee ID 2:")
    employee = manager.find_employee(2)

    if employee:
        employee.display()
    else:
        print("Employee not found.")


# ============================================================
# 4. VEHICLE INHERITANCE
# ============================================================

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."


class Car(Vehicle):
    def start(self):
        return f"Car {self.brand} {self.model} starts with a key."


class Motorcycle(Vehicle):
    def start(self):
        return f"Motorcycle {self.brand} {self.model} starts."


def challenge_4():
    print("\n=== 4. Vehicle Inheritance ===")

    vehicles = [
        Car("Toyota", "Camry"),
        Motorcycle("Honda", "Shine"),
    ]

    for vehicle in vehicles:
        print(vehicle.start())


# ============================================================
# 5. SHAPE AREA CALCULATOR
# ============================================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")

        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def challenge_5():
    print("\n=== 5. Shape Area Calculator ===")

    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(8, 4),
    ]

    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")


# ============================================================
# 6. SHOPPING CART
# ============================================================

class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        self.items.append((product, quantity))
        print(f"Added {quantity} x {product.name}.")

    def calculate_total(self):
        return sum(
            product.price * quantity
            for product, quantity in self.items
        )

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("Shopping cart:")

        for product, quantity in self.items:
            subtotal = product.price * quantity
            print(
                f"{product.name} x {quantity}: "
                f"Rs. {subtotal:.2f}"
            )

        print(f"Total: Rs. {self.calculate_total():.2f}")


def challenge_6():
    print("\n=== 6. Shopping Cart ===")

    cart = ShoppingCart()

    cart.add_product(Product("Notebook", 50), 2)
    cart.add_product(Product("Pen", 10), 3)

    cart.display_cart()


# ============================================================
# 7. MOVIE RATING SYSTEM
# ============================================================

class Movie:
    def __init__(self, title):
        self.title = title
        self.ratings = []

    def add_rating(self, rating):
        if not isinstance(rating, (int, float)) or isinstance(rating, bool):
            print("Rating must be a number.")
            return

        if not 1 <= rating <= 5:
            print("Rating must be between 1 and 5.")
            return

        self.ratings.append(rating)
        print(f"Rating {rating} added for {self.title}.")

    def average_rating(self):
        if not self.ratings:
            return 0

        return sum(self.ratings) / len(self.ratings)

    def display(self):
        print(f"Movie: {self.title}")
        print(f"Number of ratings: {len(self.ratings)}")
        print(f"Average rating: {self.average_rating():.2f}/5")


def challenge_7():
    print("\n=== 7. Movie Rating System ===")

    movie = Movie("The Python Adventure")

    movie.add_rating(4)
    movie.add_rating(5)
    movie.add_rating(3)

    movie.display()


# ============================================================
# 8. HOSPITAL PATIENT RECORDS
# ============================================================

class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        if age < 0:
            raise ValueError("Age cannot be negative.")

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def display(self):
        print(
            f"Patient ID: {self.patient_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Diagnosis: {self.diagnosis}"
        )


class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            print("Patient ID already exists.")
            return

        self.patients[patient.patient_id] = patient
        print(f"Patient {patient.name} added successfully.")

    def find_patient(self, patient_id):
        return self.patients.get(patient_id)

    def display_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        for patient in self.patients.values():
            patient.display()


def challenge_8():
    print("\n=== 8. Hospital Patient Records ===")

    hospital = Hospital()

    hospital.add_patient(
        Patient(101, "Anjali", 25, "Fever")
    )
    hospital.add_patient(
        Patient(102, "Ravi", 40, "Migraine")
    )

    print("\nAll patient records:")
    hospital.display_patients()

    print("\nSearching for patient ID 101:")
    patient = hospital.find_patient(101)

    if patient:
        patient.display()
    else:
        print("Patient not found.")


# ============================================================
# 9. SCHOOL RESULT PROCESSING
# ============================================================

class SchoolResult:
    def __init__(self, student_name, marks):
        if not marks:
            raise ValueError("At least one subject mark is required.")

        for mark in marks:
            if not isinstance(mark, (int, float)) or isinstance(mark, bool):
                raise ValueError("Marks must be numbers.")

            if not 0 <= mark <= 100:
                raise ValueError("Each mark must be between 0 and 100.")

        self.student_name = student_name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        average = self.average_marks()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 35:
            return "D"
        else:
            return "F"

    def has_passed(self):
        # Every subject must have at least 35 marks.
        return all(mark >= 35 for mark in self.marks)

    def display_result(self):
        print(f"Student: {self.student_name}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.total_marks()}")
        print(f"Average: {self.average_marks():.2f}")
        print(f"Grade: {self.grade()}")
        print(f"Result: {'Pass' if self.has_passed() else 'Fail'}")


def challenge_9():
    print("\n=== 9. School Result Processing ===")

    result = SchoolResult("Preethi", [85, 90, 78, 88, 92])
    result.display_result()


# ============================================================
# 10. ONLINE COURSE MANAGEMENT
# ============================================================

class Course:
    def __init__(self, course_id, title, instructor):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student_name):
        if not student_name.strip():
            print("Student name cannot be empty.")
            return

        if student_name in self.students:
            print(f"{student_name} is already enrolled.")
            return

        self.students.append(student_name)
        print(f"{student_name} enrolled in {self.title}.")

    def display_course(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course: {self.title}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled students: {len(self.students)}")

        if self.students:
            for student in self.students:
                print(f"- {student}")
        else:
            print("No students enrolled yet.")


def challenge_10():
    print("\n=== 10. Online Course Management ===")

    course = Course(501, "Python Programming", "Mr. Kumar")

    course.enroll_student("Preethi")
    course.enroll_student("Rahul")

    print()
    course.display_course()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    challenge_1()
    challenge_2()
    challenge_3()
    challenge_4()
    challenge_5()
    challenge_6()
    challenge_7()
    challenge_8()
    challenge_9()
    challenge_10()


if __name__ == "__main__":
    main()