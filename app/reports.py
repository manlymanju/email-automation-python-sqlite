from db import get_connection


def email_status_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(*) 
        FROM emails
        GROUP BY status
    """)
    results = cursor.fetchall()

    print("\n📊 Email Status Summary:")
    for status, count in results:
        print(f"{status}: {count}")

    conn.close()


def failed_emails_with_retries():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, recipient, retry_count
        FROM emails
        WHERE status = 'FAILED'
    """)
    results = cursor.fetchall()

    print("\n❌ Failed Emails:")
    if not results:
        print("No permanently failed emails.")
    else:
        for row in results:
            print(row)

    conn.close()


def average_retry_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(retry_count)
        FROM emails
    """)
    avg_retry = cursor.fetchone()[0]

    print(f"\n🔁 Average Retry Count: {avg_retry}")

    conn.close()


if __name__ == "__main__":
    email_status_summary()
    failed_emails_with_retries()
    average_retry_count()
