# Library Management System

## Overview

A Python command-line application that demonstrates object-oriented programming, JSON persistence, validation, exception handling, and modular design.

## Features

- Add, update, delete, and search books.
- Track book availability.
- Register and manage library members.
- Issue and return books.
- Calculate late-return fines at ₹5 per day.
- Generate available-book, borrowed-book, top-borrower, and fine reports.
- Store library data in JSON files.

## Project Structure

- `app.py` – command-line menu and application entry point.
- `book.py` – book model and book management.
- `member.py` – member model and member management.
- `issue.py` – issue transactions, returns, and fines.
- `reports.py` – library reports.
- `storage.py` – JSON persistence.
- `exceptions.py` – custom exceptions.
- `validator.py` – input validation.
- `data/` – JSON data files.

## Requirements

- Python 3.10 or later.

No third-party packages are required.

## Run the Application

Open a terminal in the `WEEK-3 Task` folder and run:

```powershell
python -m library_management.app
```

## Data Files

The application stores books, members, and issue records in:

- `library_management/data/books.json`
- `library_management/data/members.json`
- `library_management/data/issues.json`

## Concepts Demonstrated

- Classes and objects
- Encapsulation
- Composition and collaboration between objects
- Type hints and docstrings
- Exception handling
- Validation
- JSON serialization and persistence
- Separation of responsibilities across modules

## Current Limitations

- Email validation is basic.
- Fine payments and administrative workflows are not implemented.
- Automated test coverage should be added before production use.
- This application is intended as a learning project.