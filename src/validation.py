CATEGORIES = {
    "1": "Wi-Fi",
    "2": "Hostel",
    "3": "Mess",
    "4": "Maintenance",
    "5": "Cleaning",
    "6": "Other"
}

PRIORITIES = {
    "1": "Low",
    "2": "Medium",
    "3": "High"
}

STATUSES = {
    "1": "Pending",
    "2": "In Progress",
    "3": "Resolved"
}


def validate_text(value):
    return bool(value.strip())


def get_category(choice):
    return CATEGORIES.get(choice)


def get_priority(choice):
    return PRIORITIES.get(choice)


def get_status(choice):
    return STATUSES.get(choice)


def show_categories():
    print("\nCategories:")
    for key, value in CATEGORIES.items():
        print(f"{key}. {value}")


def show_priorities():
    print("\nPriority:")
    for key, value in PRIORITIES.items():
        print(f"{key}. {value}")


def show_statuses():
    print("\nStatus:")
    for key, value in STATUSES.items():
        print(f"{key}. {value}")
