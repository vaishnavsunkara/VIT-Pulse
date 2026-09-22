"""
VIT-Pulse
---------
A student-focused campus problem reporting and tracking system.
"""

from complaints import Complaint


# Get complaint details from the user
title = input("Enter complaint title: ")
description = input("Enter complaint description: ")
category = input("Enter complaint category: ")


# Create a complaint object
complaint1 = Complaint(
    title,
    description,
    category
)


# Display the complaint
complaint1.display()