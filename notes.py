# notes.py

import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(job_id, note):
    notes = load_notes()
    if job_id not in notes:
        notes[job_id] = []
    notes[job_id].append(note)
    save_notes(notes)

def get_notes(job_id):
    notes = load_notes()
    return notes.get(job_id, [])

def update_note(job_id, note_index, new_note):
    notes = load_notes()
    if job_id in notes and 0 <= note_index < len(notes[job_id]):
        notes[job_id][note_index] = new_note
        save_notes(notes)

def delete_note(job_id, note_index):
    notes = load_notes()
    if job_id in notes and 0 <= note_index < len(notes[job_id]):
        del notes[job_id][note_index]
        save_notes(notes)

# Example usage:
# add_note("123", "Interview scheduled for next week.")
# print(get_notes("123"))
