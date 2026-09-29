# VIT-Pulse

A student-focused campus problem reporting and tracking system.

## About

VIT-Pulse is a Python-based campus issue management system designed to help students report problems and allow representatives or administrators to track and manage them.

The project focuses on common campus issues such as:

- Wi-Fi problems
- Hostel maintenance
- Mess-related issues
- Cleaning and hygiene
- Electrical and maintenance problems
- Other campus facilities

## Features

### Student Portal
- Create complaints
- Select complaint category
- Set complaint priority
- View complaints
- Search complaints

### Admin / FR Portal
- View all complaints
- Search complaints
- Filter complaints by category
- Update complaint status
- View dashboard statistics

### Database
- SQLite database
- Persistent complaint storage
- Automatic complaint IDs
- Status tracking

## Technology Stack

- Python
- SQLite
- Object-Oriented Programming
- Git
- GitHub
- Python standard library only

## Project Structure

```text
VIT-Pulse/
├── src/
│   ├── main.py
│   ├── complaints.py
│   ├── database.py
│   ├── validation.py
│   └── reports.py
├── tests/
│   ├── __init__.py
│   └── test_vit_pulse.py
├── README.md
├── statement.md
├── requirements.txt
└── .gitignore
```

## Running the Project

From the project root:

```bash
python src/main.py
```

## Running Tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover the Complaint class, validation functions, search/filter/statistics functions, and SQLite database operations.

No external Python packages are required.
