class Complaint:
    def __init__(
        self,
        title,
        description,
        category,
        priority="Medium",
        status="Pending",
        complaint_id=None
    ):
        self.id = complaint_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display(self):
        print("\n" + "=" * 50)
        print(f"Complaint ID : {self.id}")
        print(f"Title        : {self.title}")
        print(f"Description  : {self.description}")
        print(f"Category     : {self.category}")
        print(f"Priority     : {self.priority}")
        print(f"Status       : {self.status}")
        print("=" * 50)
