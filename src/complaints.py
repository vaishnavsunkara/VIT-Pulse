class Complaint:
    def __init__(self, title, description, category, priority="Medium"):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "Pending"

    def display(self, complaint_id):
        print("\n" + "=" * 45)
        print(f"Complaint ID: {complaint_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Category: {self.category}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print("=" * 45)

    def update_status(self, new_status):
        self.status = new_status