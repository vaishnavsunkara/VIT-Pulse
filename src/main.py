from database import (
    add_complaint,
    create_table,
    get_complaints,
    update_status
)
from complaints import Complaint
from reports import filter_by_category, get_statistics, search_complaints
from validation import (
    get_category,
    get_priority,
    get_status,
    show_categories,
    show_priorities,
    show_statuses,
    validate_text
)


def create_new_complaint():
    print("\n--- Create New Complaint ---")

    title = input("Enter complaint title: ").strip()
    description = input("Enter complaint description: ").strip()

    if not validate_text(title) or not validate_text(description):
        print("\nTitle and description cannot be empty.")
        return

    show_categories()
    category = get_category(input("Choose category: "))

    if category is None:
        print("\nInvalid category.")
        return

    show_priorities()
    priority = get_priority(input("Choose priority: "))

    if priority is None:
        print("\nInvalid priority.")
        return

    complaint = Complaint(title, description, category, priority)
    complaint.id = add_complaint(complaint)

    print("\nComplaint created successfully!")
    print(f"Complaint ID: {complaint.id}")


def view_complaints():
    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints have been submitted yet.")
        return

    print("\n--- All Complaints ---")

    for complaint in complaints:
        complaint.display()


def search_complaints_menu():
    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    keyword = input("\nEnter search keyword: ").strip()
    results = search_complaints(complaints, keyword)

    if not results:
        print("\nNo matching complaints found.")
        return

    for complaint in results:
        complaint.display()


def filter_by_category_menu():
    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    show_categories()
    category = get_category(input("\nChoose category: "))

    if category is None:
        print("\nInvalid category.")
        return

    results = filter_by_category(complaints, category)

    print(f"\n--- {category} Complaints ---")

    if not results:
        print("\nNo complaints found in this category.")
        return

    for complaint in results:
        complaint.display()


def change_complaint_status():
    complaints = get_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    view_complaints()

    try:
        complaint_id = int(input("\nEnter complaint ID: "))
    except ValueError:
        print("\nPlease enter a valid complaint ID.")
        return

    show_statuses()
    status = get_status(input("Choose new status: "))

    if status is None:
        print("\nInvalid status choice.")
        return

    if update_status(complaint_id, status):
        print("\nComplaint status updated successfully!")
    else:
        print("\nComplaint ID not found.")


def show_statistics():
    statistics = get_statistics(get_complaints())

    print("\n" + "=" * 50)
    print("              VIT-PULSE DASHBOARD")
    print("=" * 50)
    print(f"Total Complaints : {statistics['total']}")
    print(f"Pending          : {statistics['pending']}")
    print(f"In Progress      : {statistics['in_progress']}")
    print(f"Resolved         : {statistics['resolved']}")
    print(f"High Priority    : {statistics['high_priority']}")
    print("=" * 50)


def student_menu():
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
            search_complaints_menu()
        elif choice == "4":
            break
        else:
            print("\nInvalid choice.")


def admin_menu():
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
            search_complaints_menu()
        elif choice == "3":
            filter_by_category_menu()
        elif choice == "4":
            change_complaint_status()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            break
        else:
            print("\nInvalid choice.")


def main():
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
