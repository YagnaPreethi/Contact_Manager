# Contact Manager - Python Mini Project

## Project Overview

Contact Manager is a command-line Python application that allows users to manage contact information. This project uses Object-Oriented Programming (OOP) concepts to organize contact details into a `Contact` class.

## Features

- Add new contacts
- View all contacts
- Search contacts by name, phone, or email
- Update existing contacts
- Delete contacts
- Store contact data in a JSON file
- Validate required contact information
- Handle errors using exceptions
- Use classes, objects, constructors, and methods
- Generate unique contact IDs and creation timestamps
- Run automated unit tests

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Classes and Objects
- Dataclasses
- Type Hints
- JSON
- File Handling
- Exception Handling
- unittest
- Git and GitHub

## Project Structure

- `app.py` - Main application
- `domain_models.py` - Contact domain model and validation
- `example_usage.py` - Example demonstrating the Contact class
- `test_domain_models.py` - Unit tests for the Contact model
- `contacts.json` - Stored contact data
- `DESIGN.md` - Design notes explaining class responsibilities
- `README.md` - Project documentation

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal in VS Code.
4. Run the example demonstrating the Contact model:

   `python example_usage.py`

5. To run the existing Contact Manager application, use:

   `python app.py`

## How to Run Tests

Run the following command in the project terminal:

`python -m unittest -v test_domain_models.py`

This command runs the automated tests for contact creation, required-field validation, updating contact details, contact equality, and timestamps.

## Learning Outcomes

- Practised Python classes and objects.
- Learned constructors and instance attributes.
- Used dataclasses to simplify model creation.
- Applied encapsulation and validation.
- Used methods to update contact details.
- Added type hints and documentation.
- Practised exception handling and unit testing.
- Understood domain modelling and separation of responsibilities.
- Practised Git and GitHub version control.

## Future Improvements

- Integrate the Contact class into the main application.
- Add email-format and phone-number validation.
- Improve search and duplicate-contact handling.
- Add more unit tests for the complete application.
