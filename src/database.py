"""
Database management for VIT-Pulse.

This module handles storing and retrieving complaints
using SQLite.
"""

import sqlite3


DATABASE_NAME = "vit_pulse.db"


def connect_database():
    """Connect to the VIT-Pulse database."""

    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """Create the complaints table if it does not exist."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_complaint(title, description, category, priority):
    """Save a new complaint to the database."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (title, description, category, priority, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        description,
        category,
        priority,
        "Pending"
    ))

    connection.commit()
    complaint_id = cursor.lastrowid
    connection.close()

    return complaint_id


def get_complaints():
    """Return all complaints from the database."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, description, category, priority, status
        FROM complaints
        ORDER BY id
    """)

    complaints = cursor.fetchall()
    connection.close()

    return complaints


def update_status(complaint_id, status):
    """Update the status of a complaint."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status = ?
        WHERE id = ?
    """, (status, complaint_id))

    connection.commit()
    connection.close()