# 🎯 Job Application Automation & Tracking System

Automate and streamline your job hunt with this Python-powered AI assistant.

---

## 🚀 Features

✨ **Smart Job Search**  
Search remote job boards and filter based on salary, role type, supervision level, and more.

📋 **Application Tracker**  
Track job applications, status (`Saved → Applied → Interview → Offer → Rejected`), and history in one place.

📅 **Follow-Up Reminders**  
Integrates with Outlook to auto-schedule reminders and follow-ups.

🧠 **AI-Powered**  
- Generate tailored cover letters  
- Summarize company insights  
- Suggest resume keyword improvements

🗂️ **Company Research Notes**  
Store red flags, benefits, and culture insights per job post.

📊 **Dashboard (Streamlit)**  
Easily view, filter, and manage applications from a clean web UI.

🔒 **Private & Local**  
Runs locally. All your data stays with you.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **AI API**: OpenAI GPT-4 (for cover letter generation and insights)
- **Dashboard**: Streamlit (Free, easy to host locally or on Streamlit Cloud)
- **Database**: SQLite or Google Sheets (configurable)
- **Email Integration**: Outlook via `pywin32` (Windows) or Microsoft Graph API (cross-platform)
- **Job Search**: Web scraping or API (e.g., RemoteOK, LinkedIn Jobs API)

---

## 📁 File Structure
job-automation-tracker/
│
├── .env                         # API keys and sensitive credentials (excluded from Git)
├── README.md                    # Project overview and instructions
├── requirements.txt             # Python dependencies
│
├── main.py                      # Streamlit app entry point
│
├── utils/
│   ├── ai_helper.py             # Handles OpenAI API interactions
│   ├── outlook_integration.py  # Manages email tracking with Outlook
│   ├── tracker.py              # Job application status tracking logic
│   └── data_manager.py         # Handles local storage and file I/O
│
├── data/
│   ├── applications.xlsx        # Main file for tracking job applications
│   └── notes/                   # Folder for storing company research and notes
│
└── assets/
    └── logo.png                # Optional branding/logo for Streamlit UI


---

## 🚀 Setup Instructions

1. Clone this repository
```bash
git clone https://github.com/your-username/job-automation-tracker.git
cd job-automation-tracker

2. Setup your environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Add environment variables
OPENAI_API_KEY=your_openai_key
OUTLOOK_USER=your_email@domain.com

4. Run the dashboard
streamlit run dashboard.py








