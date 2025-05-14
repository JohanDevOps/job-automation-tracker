import win32com.client as win32
import os
from datetime import datetime
from config import OUTLOOK_EMAIL_ADDRESS  # Importing the Outlook email from config.py

class EmailClient:
    def __init__(self):
        try:
            self.outlook = win32.Dispatch("Outlook.Application")
            self.namespace = self.outlook.GetNamespace("MAPI")
            self.inbox = self.namespace.GetDefaultFolder(6)  # 6 = Inbox
            self.sent_items = self.namespace.GetDefaultFolder(5)  # 5 = Sent Items
            self.email_address = OUTLOOK_EMAIL_ADDRESS  # Assign the imported email address
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Outlook: {e}")

    def send_email(self, to, subject, body, attachments=[]):
        mail = self.outlook.CreateItem(0)  # 0 = Mail Item
        mail.To = to
        mail.Subject = subject
        mail.Body = body
        for attachment in attachments:
            if os.path.exists(attachment):
                mail.Attachments.Add(attachment)
        mail.Send()
        print(f"Email sent to {to} with subject '{subject}'")

    def fetch_sent_emails(self, keyword=None, days_back=30):
        cutoff = datetime.now() - timedelta(days=days_back)
        messages = self.sent_items.Items
        messages.Sort("SentOn", True)
        results = []

        for message in messages:
            if message.SentOn < cutoff:
                break
            if keyword and keyword.lower() not in message.Subject.lower():
                continue
            results.append({
                'to': message.To,
                'subject': message.Subject,
                'sent_on': message.SentOn.strftime('%Y-%m-%d %H:%M:%S')
            })
        return results

    def check_email_sent(self, recipient_email, subject_contains=None):
        emails = self.fetch_sent_emails(keyword=subject_contains)
        return any(recipient_email.lower() in email['to'].lower() for email in emails)

# Example usage:
# email_client = EmailClient()
# email_client.send_email("example@example.com", "Test Subject", "Test Body", attachments=["resume.pdf"])
# print(f"Using Outlook email address: {email_client.email_address}")
