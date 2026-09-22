"""
Complaint data structures for VIT-Pulse.

This module will contain the data and logic related to campus complaints.
"""

class Complaint:
    """Represents a single campus complaint."""

    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.status = "Pending"

    def display(self):
        """Display the complaint information."""
        print("\n--- Complaint Details ---")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Category: {self.category}")
        print(f"Status: {self.status}")