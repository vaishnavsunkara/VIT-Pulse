"""
VIT-Pulse
---------
A student-focused campus problem reporting and tracking system.
"""

from complaints import Complaint


# Create a sample complaint
complaint1 = Complaint(
    "Wi-Fi not working",
    "Wi-Fi keeps disconnecting in Block 7A.",
    "Wi-Fi"
)

# Display the complaint
complaint1.display()