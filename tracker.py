# tracker.py

import json
import os
from datetime import datetime, timedelta

TRACKER_FILE = "data/job_tracker.json"

def load_tracker():
    if not os.path.exists(TRACKER_FILE):
        return []
    with open(TRACKER_FILE, "r") as f:
        return json.load(f)

def save_tracker(data):
    os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_job(job):
    tracker = load_tracker()
    if not any(existing["id"] == job["id"] for existing in tracker):
        tracker.append(job)
        save_tracker(tracker)

def update_job(job_id, field, value):
    tracker = load_tracker()
    for job in tracker:
        if job["id"] == job_id:
            job[field] = value
            break
    save_tracker(tracker)

def get_jobs():
    return load_tracker()

def set_follow_up(job_id, days=3):
    follow_up_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    update_job(job_id, "follow_up", follow_up_date)
