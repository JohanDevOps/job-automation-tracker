import json
from datetime import datetime

class ApplicationTracker:
    def __init__(self, file_path='applications.json'):
        self.file_path = file_path
        self.applications = self.load_applications()

    def load_applications(self):
        try:
            with open(self.file_path, 'r') as f:
                applications = json.load(f)
        except FileNotFoundError:
            applications = []
        return applications

    def save_applications(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.applications, f, indent=4)

    def add_application(self, job_title, company_name, application_date, status, follow_up_date=None, notes=None):
        new_application = {
            'job_title': job_title,
            'company_name': company_name,
            'application_date': application_date,
            'status': status,
            'follow_up_date': follow_up_date,
            'notes': notes
        }
        self.applications.append(new_application)
        self.save_applications()

    def update_status(self, job_title, company_name, new_status):
        for app in self.applications:
            if app['job_title'] == job_title and app['company_name'] == company_name:
                app['status'] = new_status
                self.save_applications()
                return True
        return False

    def add_notes(self, job_title, company_name, new_notes):
        for app in self.applications:
            if app['job_title'] == job_title and app['company_name'] == company_name:
                app['notes'] = new_notes
                self.save_applications()
                return True
        return False

# Example usage:
tracker = ApplicationTracker()

# Add a new job application
tracker.add_application(
    job_title="Data Entry Specialist",
    company_name="ABC Corp",
    application_date="2025-05-01",
    status="Applied",
    follow_up_date="2025-05-15",
    notes="Waiting for response from hiring manager."
)

# Update job application status
tracker.update_status("Data Entry Specialist", "ABC Corp", "Interview Scheduled")

# Add notes to a job application
tracker.add_notes("Data Entry Specialist", "ABC Corp", "Preparing for the interview.")
