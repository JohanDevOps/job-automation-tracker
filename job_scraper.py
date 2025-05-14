# job_scraper.py

import datetime

# For demo purposes, this returns mock job data
# Replace this with real job search integration using APIs or web scraping libraries like requests + BeautifulSoup or Selenium

def search_jobs(keywords, location="Remote", min_salary=55000):
    print("Searching for jobs...")

    # Simulated job listings
    jobs = [
        {
            "id": "job001",
            "title": "Credentialing Specialist",
            "company": "HealthNet Corp",
            "location": "Remote",
            "salary": "$58,000",
            "posted_date": datetime.date.today().isoformat(),
            "status": "Not Applied",
            "notes": "",
            "cover_letter_sent": False,
            "follow_up": "",
        },
        {
            "id": "job002",
            "title": "Remote Data Entry Clerk",
            "company": "FastForms LLC",
            "location": "Remote",
            "salary": "$56,500",
            "posted_date": datetime.date.today().isoformat(),
            "status": "Not Applied",
            "notes": "",
            "cover_letter_sent": False,
            "follow_up": "",
        }
    ]

    return [job for job in jobs if int(job["salary"].replace("$", "").replace(",", "")) >= min_salary]
