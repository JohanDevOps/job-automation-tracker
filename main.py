from job_scraper import search_jobs
from tracker import JobTracker
from reminder import ReminderManager
from notes import NotesManager
from email_integration import OutlookClient
from ai_helper import AIAssistant
from dashboard import run_dashboard

def main():
    print("Welcome to the Job Automation App!\n")

    # Initialize all components
    tracker = JobTracker()
    reminder = ReminderManager(tracker)
    notes = NotesManager()
    outlook = OutlookClient()
    ai = AIAssistant()

    # Search for new jobs (you can schedule or trigger this manually)
    jobs = search_jobs(keywords=["Credentialing Specialist", "Data Entry", "Verification"],
                       location="Remote",
                       min_salary=55000)

    print(f"\nFound {len(jobs)} new jobs matching criteria.\n")

    for job in jobs:
        if not tracker.is_duplicate(job):
            tracker.add_application(job)
            print(f"Added job: {job['title']} at {job['company']}")

    # Launch dashboard (e.g., in browser)
    run_dashboard()

if __name__ == "__main__":
    main()
