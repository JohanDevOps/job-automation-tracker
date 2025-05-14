import os

# Configuration settings for the job application automation system

# File paths
APPLICATIONS_FILE_PATH = "applications.json"  # Path to store job applications data
LOG_FILE_PATH = "job_application_log.txt"    # Path for logging activities

# Email Settings (used in email_integration.py)
OUTLOOK_EMAIL_ADDRESS = "johan.ospina@outlook.com"  # Your Outlook email address (set up properly in email_integration.py)

# API Keys
OPENAI_API_KEY = "your-openai-api-key"  # OpenAI API Key (if applicable)

# Reminder settings (default times, intervals)
DEFAULT_REMINDER_DAYS = 3  # Default number of days to set a reminder before follow-up

# Max jobs to display in the dashboard
MAX_JOBS_DISPLAYED = 20  # Default number of jobs to show in the dashboard (can be adjusted)

# Job Status Mapping (customizable)
STATUS_OPTIONS = ["Applied", "Interviewing", "Offer", "Rejected", "Follow-up"]

# Logging level (can adjust if needed for debug, info, etc.)
LOG_LEVEL = "INFO"

# Other global settings
REMOTE_JOB_ONLY = True  # Default setting to filter jobs by remote
MIN_SALARY = 55000      # Minimum salary for job applications

# Path to store the dashboard charts (if needed)
CHARTS_SAVE_PATH = "charts/"

# Customizable settings for job scraping and application tracking
SCRAPE_INTERVAL_DAYS = 7  # Default interval for scraping job boards (in days)
