import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import database
from complaints import Complaint
from reports import filter_by_category, get_statistics, search_complaints
from validation import (
    get_category,
    get_priority,
    get_status,
    validate_text
)


class TestVITPulse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_directory = tempfile.TemporaryDirectory()
        cls.database_path = os.path.join(
            cls.temp_directory.name,
            "test_vit_pulse.db"
        )
        database.DATABASE_NAME = cls.database_path
        database.create_table()

    @classmethod
    def tearDownClass(cls):
        cls.temp_directory.cleanup()

    def setUp(self):
        database.clear_complaints()

    def test_create_and_read_complaint(self):
        complaint = Complaint(
            "Wi-Fi not working",
            "Wi-Fi keeps disconnecting.",
            "Wi-Fi",
            "High"
        )

        complaint.id = database.add_complaint(complaint)
        complaints = database.get_complaints()

        self.assertEqual(len(complaints), 1)
        self.assertEqual(complaints[0].title, "Wi-Fi not working")
        self.assertEqual(complaints[0].status, "Pending")

    def test_update_status(self):
        complaint = Complaint(
            "Mess issue",
            "Food quality needs improvement.",
            "Mess"
        )

        complaint_id = database.add_complaint(complaint)

        self.assertTrue(
            database.update_status(complaint_id, "Resolved")
        )

        complaints = database.get_complaints()
        self.assertEqual(complaints[0].status, "Resolved")

    def test_search_and_filter(self):
        complaints = [
            Complaint("Wi-Fi issue", "Network problem", "Wi-Fi", "High"),
            Complaint("Room cleaning", "Cleaning required", "Cleaning"),
            Complaint("Mess food", "Food issue", "Mess")
        ]

        search_results = search_complaints(complaints, "network")
        category_results = filter_by_category(complaints, "Mess")

        self.assertEqual(len(search_results), 1)
        self.assertEqual(len(category_results), 1)

    def test_statistics(self):
        complaints = [
            Complaint("A", "Issue A", "Hostel", "High", "Pending"),
            Complaint("B", "Issue B", "Mess", "Medium", "In Progress"),
            Complaint("C", "Issue C", "Wi-Fi", "High", "Resolved")
        ]

        statistics = get_statistics(complaints)

        self.assertEqual(statistics["total"], 3)
        self.assertEqual(statistics["pending"], 1)
        self.assertEqual(statistics["in_progress"], 1)
        self.assertEqual(statistics["resolved"], 1)
        self.assertEqual(statistics["high_priority"], 2)

    def test_validation(self):
        self.assertTrue(validate_text("Wi-Fi problem"))
        self.assertFalse(validate_text("   "))
        self.assertEqual(get_category("1"), "Wi-Fi")
        self.assertEqual(get_priority("3"), "High")
        self.assertEqual(get_status("2"), "In Progress")
        self.assertIsNone(get_category("9"))


if __name__ == "__main__":
    unittest.main()
