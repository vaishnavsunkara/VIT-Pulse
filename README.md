# VIT-Pulse

A student-focused campus problem reporting and tracking system.

## About

VIT-Pulse is a Python-based campus issue management system designed to help students report problems and allow representatives or administrators to track and manage them.

The project focuses on common campus issues such as:

- Wi-Fi problems
- Hostel maintenance
- Mess-related issues
- Electrical problems
- Cleaning and hygiene
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
- View complaint statistics

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

## Project Structure

```text
VIT-Pulse/
│
├── src/
│   ├── main.py
│   ├── complaints.py
│   ├── database.py
│   ├── validation.py
│   └── reports.py
│
├── tests/
│   └── test_vit_pulse.py
│
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

```bash
python -m unittest discover -s tests -v
```

The project uses only Python standard-library modules, so no external packages are required.
