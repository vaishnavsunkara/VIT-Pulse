import sqlite3

from complaints import Complaint


DATABASE_NAME = "vit_pulse.db"


def connect_database():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
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


def add_complaint(complaint):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (title, description, category, priority, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        complaint.title,
        complaint.description,
        complaint.category,
        complaint.priority,
        complaint.status
    ))

    connection.commit()
    complaint_id = cursor.lastrowid
    connection.close()

    return complaint_id


def get_complaints():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, description, category, priority, status
        FROM complaints
        ORDER BY id
    """)

    rows = cursor.fetchall()
    connection.close()

    complaints = []

    for row in rows:
        complaints.append(
            Complaint(
                title=row[1],
                description=row[2],
                category=row[3],
                priority=row[4],
                status=row[5],
                complaint_id=row[0]
            )
        )

    return complaints


def update_status(complaint_id, status):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status = ?
        WHERE id = ?
    """, (status, complaint_id))

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    return updated


def clear_complaints():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM complaints")

    connection.commit()
    connection.close()
