from db import get_connection

def insert_test_emails():
    conn = get_connection()
    cursor = conn.cursor()

    emails = [
        ("test@example.com", "Welcome Email", "Welcome to our CPaaS Email Platform!"),
        ("user1@example.com", "Retry Test", "This email is for retry testing."),
        ("user2@example.com", "System Update", "Your system update is complete.")
    ]

    cursor.executemany(
        """
        INSERT INTO emails (recipient, subject, body, status)
        VALUES (?, ?, ?, 'PENDING')
        """,
        emails
    )

    conn.commit()
    conn.close()

    print("Test emails inserted successfully.")

if __name__ == "__main__":
    insert_test_emails()
