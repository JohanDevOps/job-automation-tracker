import streamlit as st
import json
import os

# Load application data
def load_applications():
    if os.path.exists("applications.json"):
        with open("applications.json", "r") as file:
            return json.load(file)
    return []

# Display job applications in a table
def display_jobs(applications):
    st.subheader("Job Applications Overview")
    
    if applications:
        # Display application statuses in a table
        data = []
        for app in applications:
            data.append({
                "Job Title": app["job_title"],
                "Company": app["company_name"],
                "Status": app["status"],
                "Last Updated": app["last_updated"],
                "Notes": ", ".join(app["notes"]) if app["notes"] else "No notes"
            })
        
        st.write(data)
    else:
        st.write("No job applications available.")

# Dashboard UI
def dashboard():
    # Application data
    applications = load_applications()
    
    # Job applications table
    display_jobs(applications)
    
    # Add more interactivity (like filters, reminders, etc.) as needed
    # Example: Show status filters (e.g., Applied, Interviewing, etc.)
    status_filter = st.selectbox("Filter by Status", options=["All", "Applied", "Interview", "Offer", "Rejected"])
    
    if status_filter != "All":
        filtered_apps = [app for app in applications if app["status"] == status_filter]
        display_jobs(filtered_apps)
    else:
        display_jobs(applications)

if __name__ == "__main__":
    dashboard()
