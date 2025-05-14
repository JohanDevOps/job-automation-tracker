# test.py

from data.applications import ApplicationTracker
from email_integration import EmailClient

# Test the ApplicationTracker
tracker = ApplicationTracker()

# Add a new job application
tracker.add_application(
    job_title="Credentialing Specialist",
    company_name="XYZ Healthcare",
    application_date="2025-05-01",
    status="Applied",
    follow_up_date="2025-05-15",
    notes="Waiting for response."
)

# Update the application status
tracker.update_status("Credentialing Specialist", "XYZ Healthcare", "Interview Scheduled")

# Add notes to the application
tracker.add_notes("Credentialing Specialist", "XYZ Healthcare", "Second round of interviews.")

# Test Email sending
email_client = EmailClient()
email_client.send_email(
    to="example@example.com", 
    subject="Test Subject", 
    body="Test Body", 
    attachments=["resume.pdf"]
)

# Check if the email was sent
email_sent = email_client.check_email_sent("example@example.com", "Test Subject")
print(f"Email sent: {email_sent}")
