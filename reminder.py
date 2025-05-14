# reminder.py

from datetime import datetime, timedelta
import json
import os

REMINDER_FILE = "reminders.json"

def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []
    with open(REMINDER_FILE, "r") as file:
        return json.load(file)

def save_reminders(reminders):
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)

def add_reminder(job_id, message, days_from_now=3):
    reminders = load_reminders()
    due_date = (datetime.now() + timedelta(days=days_from_now)).strftime("%Y-%m-%d")
    reminders.append({
        "job_id": job_id,
        "message": message,
        "due_date": due_date
    })
    save_reminders(reminders)

def get_due_reminders():
    reminders = load_reminders()
    today = datetime.now().strftime("%Y-%m-%d")
    return [r for r in reminders if r["due_date"] <= today]

def clear_reminder(job_id):
    reminders = load_reminders()
    reminders = [r for r in reminders if r["job_id"] != job_id]
    save_reminders(reminders)

# Example usage:
# add_reminder("123", "Follow up with Company ABC", days_from_now=5)
# print(get_due_reminders())
