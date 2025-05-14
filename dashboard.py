import streamlit as st
from tracker import load_applications, save_applications

apps = load_applications()
st.title("Job Application Tracker")

for app in apps:
    with st.expander(app["title"] + " at " + app["company"]):
        st.write("Location:", app["location"])
        st.write("Salary:", app["salary"])
        st.write("Link:", app["link"])
        notes = st.text_area("Notes", value=app["notes"])
        app["notes"] = notes
        if st.button("Mark as Applied", key=app["link"]):
            app["applied"] = True

save_applications(apps)
