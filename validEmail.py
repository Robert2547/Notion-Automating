from datetime import datetime, timezone
import os, json, requests
from gpt.statusGPT import getGPT
from joblist import add_job



def validEmail(email_text):
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    try:
        job_json = getGPT(email_text)
        print("GPT is working\n\n")
        print(job_json)
    
        # Removing the extraneous `json` and backticks
        clean_json = job_json.replace('json', '').strip().strip('`')

        data = json.loads(clean_json) # Convert the JSON string to a dictionary
        print("\n\n" + data)

        if data.get("Joblist", "no").lower() == "no" and data.get("Status", "no").lower() == "no": 
            print("This email is neither a job listing nor a status update")
            #deleteEmail(result, service) # Delete the email
        elif data.get("Joblist", "no").lower() == "yes":
            print("This email is a job listing")
            add_job(data, published_date) # Add the job to Notion
        elif data.get("Status", "no").lower() == "yes":
            print("This email is a status update")

    except Exception as error:
        print(f"An error occurred: {error}")
        return
