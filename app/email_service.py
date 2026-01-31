import time
from db import get_connection

MAX_RETRIES = 2


def send_pending_emails():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, recipient FROM emails WHERE status = 'PENDING'"
    )
    emails = cursor.fetchall()

    if not emails:
        print("No PENDING emails found.")

    for email_id, recipient in emails:
        print(f"Sending email {email_id} to {recipient}...")
        time.sleep(1)

        cursor.execute(
            "UPDATE emails SET status = 'FAILED', retry_count = retry_count + 1 WHERE id = ?",
            (email_id,)
        )

        print(f"Email {email_id} failed. Retry count increased.")

    conn.commit()
    conn.close()


def retry_failed_emails():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, recipient, retry_count
        FROM emails
        WHERE status = 'FAILED' AND retry_count < ?
        """,
        (MAX_RETRIES,)
    )
    emails = cursor.fetchall()

    if not emails:
        print("No emails eligible for retry.")

    for email_id, recipient, retry_count in emails:
        print(f"Retrying email {email_id} (attempt {retry_count + 1})...")
        time.sleep(1)

        cursor.execute(
            "UPDATE emails SET status = 'SENT' WHERE id = ?",
            (email_id,)
        )

        print(f"Email {email_id} SENT successfully.")

    conn.commit()
    conn.close()
