# ai_helper.py

import openai
import os

# Load API key from environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_job_description(description):
    prompt = f"Summarize this job description in 3 bullet points:\n\n{description}"
    return call_openai(prompt)

def generate_cover_letter(company, role, notes=""):
    prompt = (
        f"Write a professional but concise cover letter for the role of '{role}' at '{company}'. "
        f"Focus on remote work, attention to detail, and project management experience. "
        f"Include this context:\n{notes}"
    )
    return call_openai(prompt)

def generate_follow_up(company, role):
    prompt = (
        f"Write a polite follow-up email for a job application for the role of '{role}' at '{company}'. "
        f"Keep it short, professional, and appreciative."
    )
    return call_openai(prompt)

def call_openai(prompt, model="gpt-4", max_tokens=300):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for job seekers."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"⚠️ Error with OpenAI API: {e}"
