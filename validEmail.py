from datetime import datetime, timezone
import json
from application import add_application
from gpt.statusGPT import getGPT
from joblist import add_job


def validEmail(email_text):
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    try:
        job_json = getGPT(email_text)  # Get the JSON string from GPT-3
        # Removing the extraneous `json` and backticks
        clean_json = job_json.replace("json", "").strip().strip("`")

        data = json.loads(clean_json)  # Convert the JSON string to a dictionary

        print("\n\nProcessing the email...")
        moveFolder = 0

        if data.get("JobList") == "No" and data.get("Application") == "No":
            print("This email is neither a job listing nor a status update")
            # deleteEmail(result, service) # Delete the email
        elif (data.get("JobList") or "No") == "Yes":
            print("This email is a job listing")
            moveFolder = add_job(data, published_date)  # Add the job to Notion
        elif (data.get("Application") or "No") == "Yes":
            print("This email is a application/status update")
            moveFolder = add_application(data, published_date)  # Add the application to Notion
        return moveFolder
    
    except Exception as error:
        print(f"An error occurred in validEmail function: {error}")
        return
