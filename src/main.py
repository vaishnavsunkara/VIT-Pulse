"""
VIT-Pulse
---------
A student-focused campus problem reporting and tracking system.
"""

from database import (
    create_table,
    add_complaint,
    get_complaints,
    update_status
)


def create_new_complaint():
    """Create and save a new complaint."""

    print("\n--- Create New Complaint ---")

    title = input("Enter complaint title: ").strip()
    description = input("Enter complaint description: ").strip()

    print("\nCategories:")
    print("1. Wi-Fi")
    print("2. Hostel")
    print("3. Mess")
    print("4. Maintenance")
    print("5. Cleaning")
    print("6. Other")

    category_choice = input("Choose category: ")

    categories = {
        "1": "Wi-Fi",
        "2": "Hostel",
        "3": "Mess",
        "4": "Maintenance",
        "5": "Cleaning",
        "6": "Other"
    }

    category = categories.get(category_choice, "Other")

    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Choose priority: ")

    priorities = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    priority = priorities.get(priority_choice, "Medium")

    if not title or not description:
        print("\nTitle and description cannot be empty.")
        return

    complaint_id = add_complaint(
        title,
        description,
        category,
        priority
    )

    print("\nComplaint created successfully!")
    print(f"Complaint ID: {complaint_id}")


def display_complaint(complaint):
    """Display one complaint."""

    complaint_id, title, description, category, priority, status = complaint

    print("\n" + "=" * 50)
    print(f"Complaint ID : {complaint_id}")
    print(f"Title        : {title}")
    print(f"Description  : {description}")
    print(f"Category     : {category}")
    print(f"Priority     : {priority}")
    print(f"Status       : {status}")
    print("=" * 50)


def view_complaints():
    """Display all complaints."""

    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints have been submitted yet.")
        return

    print("\n--- All Complaints ---")

    for complaint in complaints:
        display_complaint(complaint)


def search_complaints():
    """Search complaints by keyword."""

    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    keyword = input("\nEnter search keyword: ").strip().lower()

    found = False

    for complaint in complaints:
        _, title, description, category, _, status = complaint

        if (
            keyword in title.lower()
            or keyword in description.lower()
            or keyword in category.lower()
            or keyword in status.lower()
        ):
            display_complaint(complaint)
            found = True

    if not found:
        print("\nNo matching complaints found.")


def filter_by_category():
    """Display complaints belonging to a selected category."""

    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    print("\nCategories:")
    print("1. Wi-Fi")
    print("2. Hostel")
    print("3. Mess")
    print("4. Maintenance")
    print("5. Cleaning")
    print("6. Other")

    categories = {
        "1": "Wi-Fi",
        "2": "Hostel",
        "3": "Mess",
        "4": "Maintenance",
        "5": "Cleaning",
        "6": "Other"
    }

    choice = input("\nChoose category: ")

    if choice not in categories:
        print("\nInvalid category.")
        return

    selected_category = categories[choice]
    found = False

    print(f"\n--- {selected_category} Complaints ---")

    for complaint in complaints:
        if complaint[3] == selected_category:
            display_complaint(complaint)
            found = True

    if not found:
        print("\nNo complaints found in this category.")


def change_complaint_status():
    """Update complaint status."""

    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    view_complaints()

    try:
        complaint_id = int(input("\nEnter complaint ID: "))

        print("\n1. Pending")
        print("2. In Progress")
        print("3. Resolved")

        choice = input("Choose new status: ")

        statuses = {
            "1": "Pending",
            "2": "In Progress",
            "3": "Resolved"
        }

        if choice not in statuses:
            print("\nInvalid status choice.")
            return

        update_status(complaint_id, statuses[choice])

        print("\nComplaint status updated successfully!")

    except ValueError:
        print("\nPlease enter a valid complaint ID.")


def show_statistics():
    """Display complaint statistics."""

    complaints = get_complaints()

    total = len(complaints)
    pending = 0
    in_progress = 0
    resolved = 0
    high_priority = 0

    for complaint in complaints:
        priority = complaint[4]
        status = complaint[5]

        if status == "Pending":
            pending += 1
        elif status == "In Progress":
            in_progress += 1
        elif status == "Resolved":
            resolved += 1

        if priority == "High":
            high_priority += 1

    print("\n" + "=" * 50)
    print("              VIT-PULSE DASHBOARD")
    print("=" * 50)
    print(f"Total Complaints : {total}")
    print(f"Pending          : {pending}")
    print(f"In Progress      : {in_progress}")
    print(f"Resolved         : {resolved}")
    print(f"High Priority    : {high_priority}")
    print("=" * 50)


def student_menu():
    """Display the student menu."""

    while True:
        print("\n" + "=" * 50)
        print("             STUDENT PORTAL")
        print("=" * 50)

        print("\n1. Create Complaint")
        print("2. View Complaints")
        print("3. Search Complaints")
        print("4. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_new_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            search_complaints()
        elif choice == "4":
            break
        else:
            print("\nInvalid choice.")


def admin_menu():
    """Display the admin/FR menu."""

    while True:
        print("\n" + "=" * 50)
        print("             ADMIN / FR PORTAL")
        print("=" * 50)

        print("\n1. View All Complaints")
        print("2. Search Complaints")
        print("3. Filter by Category")
        print("4. Update Complaint Status")
        print("5. Dashboard Statistics")
        print("6. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_complaints()
        elif choice == "2":
            search_complaints()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            change_complaint_status()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            break
        else:
            print("\nInvalid choice.")


def main():
    """Start the VIT-Pulse application."""

    create_table()

    while True:
        print("\n" + "=" * 50)
        print("                 VIT-PULSE")
        print("     Campus Problem Reporting System")
        print("=" * 50)

        print("\n1. Student Portal")
        print("2. Admin / FR Portal")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("\nThank you for using VIT-Pulse!")
            break
        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()