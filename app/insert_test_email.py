from email_service import create_email

create_email(
    "test@example.com",
    "Welcome",
    "Hello from CPaaS Email System"
)

create_email(
    "user1@example.com",
    "Stage 4 Test",
    "This email is for retry testing"
)

print("Test emails inserted.")
