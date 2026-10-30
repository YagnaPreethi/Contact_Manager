# Python OOP Fundamentals   Story-1(26-10-26)

## 1. Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming approach that organizes code around **classes and objects**.

OOP helps us organize related data and functions together, making applications easier to maintain, reuse, test, and extend.

### Main OOP concepts

- Class
- Object
- Constructor (`__init__`)
- Instance variables
- Class variables
- Instance methods
- Class methods
- Static methods
- `self` and `cls`
- Object lifecycle

### Real-world example

Consider a contact management application.

Each contact has information such as a name, phone number, and email address. Each contact can also perform operations, such as displaying its details.

A Python class can represent a contact, and individual contacts can be represented as objects.

---

## 2. Classes and Objects

### 2.1 What is a class?

A class is a blueprint for creating objects.

It defines the data and behavior that objects of that class can have.

### 2.2 What is an object?

An object is an instance of a class.

Each object can have its own data while sharing the behavior defined by the class.

### Example

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")


contact1 = Contact("Anu", "9876543210")
contact2 = Contact("Ravi", "9123456780")

contact1.display()
contact2.display()
```

### Output

```text
Name: Anu
Phone: 9876543210
Name: Ravi
Phone: 9123456780
```

### Explanation

- `Contact` is the class.
- `contact1` and `contact2` refer to separate objects.
- `name` and `phone` store each contact's information.
- `display()` is a method that displays the contact's information.

### Diagram

```text
              Contact Class
             /             \
            /               \
     Contact Object 1    Contact Object 2
       name = Anu          name = Ravi
       phone = ...         phone = ...
```

### Real-world example

A `Contact` class is like a contact form template. Each saved contact is a separate instance created from that template.

---

## 3. Constructors: `__init__()`

A constructor-like initialization method is used to initialize an object's attributes when the object is created.

In Python, `__init__()` is called automatically after the object's instance has been created.

Technically, `__new__()` creates the instance, while `__init__()` initializes it.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Priya", 21)

print(student1.name)
print(student1.age)
```

### Output

```text
Priya
21
```

### Explanation

When Python executes:

```python
student1 = Student("Priya", 21)
```

Python creates a `Student` instance and initializes its attributes through `__init__()`.

The values are stored as:

```python
student1.name = "Priya"
student1.age = 21
```

### Why use `__init__()`?

- To initialize object attributes.
- To assign initial values.
- To ensure an object starts with the required information.
- To make object creation easier and more consistent.

### Example with default values

```python
class Contact:
    def __init__(self, name, phone="Not provided"):
        self.name = name
        self.phone = phone


contact1 = Contact("Anu")
contact2 = Contact("Ravi", "9876543210")

print(contact1.phone)
print(contact2.phone)
```

Output:

```text
Not provided
9876543210
```

---

## 4. Instance Variables and Class Variables

Variables in a class can belong to individual objects or be shared through the class.

### 4.1 Instance variables

Instance variables store information specific to an individual object.

They are commonly assigned through `self` inside `__init__()`.

### Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Arun", 30000)
emp2 = Employee("Meena", 40000)

print(emp1.name)
print(emp2.name)
```

Output:

```text
Arun
Meena
```

Each employee has a separate `name` and `salary`.

### 4.2 Class variables

A class variable is defined in the class body and is normally shared by instances through the class.

### Example

```python
class Employee:
    company = "BlackRoth"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Arun")
emp2 = Employee("Meena")

print(emp1.company)
print(emp2.company)
print(Employee.company)
```

Output:

```text
BlackRoth
BlackRoth
BlackRoth
```

Both employees can access the same class-level company name.

### Important distinction

If an attribute is assigned through an instance, Python generally creates or updates an instance attribute rather than changing the class attribute.

```python
emp1.company = "Other Company"

print(emp1.company)
print(emp2.company)
print(Employee.company)
```

Output:

```text
Other Company
BlackRoth
BlackRoth
```

Here, `emp1.company` refers to the instance attribute that shadows the class attribute.

To change the shared class attribute, use:

```python
Employee.company = "New Company"
```

### Comparison

| Feature | Instance variable | Class variable |
|---|---|---|
| Belongs to | Individual object | Class |
| Typical location | Inside `__init__()` | Class body |
| Common access | `self.name` | `ClassName.company` |
| Values | Can differ between objects | Shared unless shadowed |
| Example | Employee name | Company name |

### Real-world example

In an employee management system:

- Employee name is an instance variable.
- Employee ID is usually an instance variable.
- A company-wide policy or company name can be a class variable if it is genuinely shared by the objects.

---

## 5. Instance Methods

An instance method operates on a particular object.

It takes `self` as its first parameter by convention.

Through `self`, the method can access or modify the object's instance attributes.

### Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f"Balance: {self.balance}")


account = BankAccount("Priya", 1000)

account.deposit(500)
account.display_balance()
```

Output:

```text
Balance: 1500
```

### Explanation

- `deposit()` changes the balance of a particular account.
- `display_balance()` displays that account's balance.
- `self.balance` refers to the balance belonging to the current object.

In a real banking application, deposits would also require validation, transaction records, and other safeguards.

---

## 6. Class Methods

A class method operates on the class rather than on a particular instance.

It uses the `@classmethod` decorator and conventionally takes `cls` as its first parameter.

### Example

```python
class Employee:
    company = "BlackRoth"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company_name):
        cls.company = company_name


emp1 = Employee("Anu")
emp2 = Employee("Ravi")

Employee.change_company("Example Technologies")

print(emp1.company)
print(emp2.company)
```

Output:

```text
Example Technologies
Example Technologies
```

### Explanation

- `@classmethod` makes the method a class method.
- `cls` refers to the class through which the method is called.
- `cls.company` accesses the class-level attribute.
- Changing `cls.company` changes the shared class attribute in this example.

### Alternative constructor example

Class methods are also useful for creating objects from alternative input formats.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name.strip(), int(age))


student = Student.from_string("Anu, 21")

print(student.name)
print(student.age)
```

Output:

```text
Anu
21
```

This class method creates a student from a comma-separated string.

---

## 7. Static Methods

A static method is a utility function grouped inside a class because it is related to that class's purpose.

It uses the `@staticmethod` decorator and does not automatically receive `self` or `cls`.

### Example

```python
class Contact:
    @staticmethod
    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) == 10


print(Contact.is_valid_phone("9876543210"))
print(Contact.is_valid_phone("98AB"))
```

Output:

```text
True
False
```

### Explanation

- `@staticmethod` defines the method as a static method.
- `is_valid_phone()` receives only the supplied `phone` argument.
- It does not need access to an object's state or the class's state.

This example performs only a basic format check. Real phone-number validation may need to support country codes and different national numbering rules.

### When should you use a static method?

Use one when a function logically belongs to a class but does not need instance-specific or class-specific information.

---

## 8. Understanding `self` and `cls`

### 8.1 What is `self`?

`self` refers to the current instance when an instance method is called.

It is a naming convention rather than a reserved Python keyword.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student1 = Student("Anu")
student2 = Student("Ravi")

student1.display()
student2.display()
```

Output:

```text
Anu
Ravi
```

The same `display()` method works with different objects because `self` refers to the instance receiving the call.

### 8.2 What is `cls`?

`cls` is the conventional first parameter of a class method. It refers to the class.

### Example

```python
class Counter:
    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)


Counter.show_count()
```

Output:

```text
0
```

### Comparison

| Feature | `self` | `cls` |
|---|---|---|
| Refers to | Current instance | Class |
| Used in | Instance methods | Class methods |
| Accesses | Instance and accessible class attributes | Class attributes and class-level behavior |
| Automatically supplied? | Yes, for normal instance-method calls | Yes, for class-method calls |
| Typical example | `self.name` | `cls.count` |

### Important note

Neither `self` nor `cls` is a Python keyword. They are conventions that make code easier to understand.

---

## 9. Instance Methods vs Class Methods vs Static Methods

| Feature | Instance method | Class method | Static method |
|---|---|---|---|
| Decorator | None required | `@classmethod` | `@staticmethod` |
| First parameter | `self` by convention | `cls` by convention | No automatic first parameter |
| Instance state | Can access it through `self` | Not automatically given an instance | Not automatically given an instance |
| Class state | Can access it through the class or instance | Can access it through `cls` | No automatic class reference |
| Common purpose | Object-specific operations | Class-level operations or alternative constructors | Related utility functions |
| Example | `deposit()` | `change_company()` | `is_valid_phone()` |

### Simple memory trick

- **Instance method:** Works with an individual object.
- **Class method:** Works with the class.
- **Static method:** Provides a related utility without automatically receiving an object or class.

---

## 10. Object Lifecycle

The object lifecycle describes the stages an object goes through during its existence.

### Typical stages

1. **Creation:** Python creates an instance.
2. **Initialization:** `__init__()` initializes its attributes.
3. **Use:** The object participates in operations and method calls.
4. **Becomes unreachable:** No accessible references remain to the object.
5. **Cleanup:** Python manages memory; finalization may occur, but its timing is not generally guaranteed.

### Diagram

```text
        Class Definition
               |
               v
        Object Creation
               |
               v
      __init__() Called
               |
               v
          Object Used
               |
               v
      References Removed
               |
               v
     Object Becomes Unreachable
               |
               v
      Garbage Collection
        When Appropriate
```

### Example

```python
class Demo:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} initialized")


obj = Demo("Example")

print(obj.name)

del obj
```

Possible output:

```text
Example initialized
Example
```

The `del obj` statement removes the name `obj`. If no other references remain, the instance becomes eligible for garbage collection.

### What about `__del__()`?

Python supports a special method named `__del__()` that may be used for finalization.

However, its execution timing is not guaranteed, and it is not a reliable way to manage important resources. Use context managers, such as `with open(...)`, for resources that require dependable cleanup.

---

## 11. Practical Example: Contact Manager

A Contact Manager is a useful real-world example of OOP.

### Requirements

Each contact has:

- Name
- Phone number
- Email address

Each contact can:

- Display its information.
- Update its information.

### Example implementation

```python
class Contact:
    application_name = "Contact Manager"

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def update_email(self, new_email):
        self.email = new_email

    @classmethod
    def get_application_name(cls):
        return cls.application_name

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email.split("@")[-1]


contact = Contact(
    "Anu",
    "9876543210",
    "anu@example.com"
)

contact.display()

contact.update_email("anu.new@example.com")

print(contact.email)
print(Contact.get_application_name())
print(Contact.is_valid_email("anu@example.com"))
```

### Output

```text
Name: Anu
Phone: 9876543210
Email: anu@example.com
anu.new@example.com
Contact Manager
True
```

### Concepts demonstrated

| OOP concept | Example |
|---|---|
| Class | `Contact` |
| Object | `contact` |
| Constructor | `__init__()` |
| Instance variables | `name`, `phone`, `email` |
| Class variable | `application_name` |
| Instance method | `display()` |
| Instance method modifying state | `update_email()` |
| Class method | `get_application_name()` |
| Static method | `is_valid_email()` |

The email check is intentionally simple and is not a complete email-validation solution.

In your full Contact Manager project, contact management and persistence should remain in their appropriate service and repository modules rather than being placed entirely inside the `Contact` model.

---

## 12. Advantages of OOP

1. **Code organization:** Related data and behavior can be grouped together.
2. **Reusability:** Classes can be reused to create many objects.
3. **Maintainability:** Clear responsibilities make code easier to update.
4. **Encapsulation:** An interface can control how an object's state is accessed or changed.
5. **Extensibility:** Classes can be extended when requirements change.
6. **Testability:** Small, focused classes and methods can be tested independently.

OOP is useful for many applications, but it is not necessary for every small program. Simple functions may be a better choice for straightforward tasks.

---

## 13. Common Beginner Mistakes

### Mistake 1: Forgetting `self`

Incorrect:

```python
class Student:
    def __init__(name):
        name = name
```

Correct:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### Mistake 2: Calling an instance method incorrectly

Incorrect:

```python
class Student:
    def display(self):
        print("Hello")


Student.display()
```

This normally raises a `TypeError` because no instance was supplied.

Correct:

```python
student = Student()
student.display()
```

### Mistake 3: Confusing instance and class variables

Incorrect assumption: Changing `student1.name` changes every student's name.

In reality, each instance can have its own `name`.

### Mistake 4: Using `self` in a static method

A static method does not automatically receive `self`.

Incorrect:

```python
@staticmethod
def display(self):
    print(self.name)
```

A static method should not depend on an automatically supplied instance. Use an instance method if the operation needs `self.name`.

### Mistake 5: Assuming `__init__()` creates the instance

`__new__()` is responsible for creating the instance, while `__init__()` initializes it.

---

## 14. Quick Revision Questions

1. What is a class?
2. What is an object?
3. What is the purpose of `__init__()`?
4. What is the difference between an instance variable and a class variable?
5. What does `self` refer to?
6. What does `cls` refer to?
7. When should you use an instance method?
8. When should you use a class method?
9. When should you use a static method?
10. What happens when an object becomes unreachable?

### Practice exercise

Create an `Employee` class with:

- Instance variables: `name`, `employee_id`, and `salary`.
- A class variable: `company_name`.
- An instance method: `display_details()`.
- A class method: `change_company_name()`.
- A static method: `is_valid_employee_id()`.

Create two employee objects and test all three method types.

---

## 15. Conclusion

Object-Oriented Programming helps organize Python programs around objects that combine data and behavior.

Understanding classes, objects, constructors, variables, methods, `self`, `cls`, and object lifecycle provides a strong foundation for building maintainable applications such as a Contact Manager.