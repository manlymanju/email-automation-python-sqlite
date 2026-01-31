from email_service import send_pending_emails, retry_failed_emails

if __name__ == "__main__":
    print("Main started...")

    print("Processing pending emails...")
    send_pending_emails()

    print("Retrying failed emails...")
    retry_failed_emails()

    print("Main finished.")
