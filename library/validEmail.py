from datetime import datetime, timezone
import json
from library.application import add_application
from gpt.statusGPT import getGPT
from library.joblist import add_job
from library.gmail import moveEmailToFolder


def validEmail(email_text, subject, category, service, email_id):
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    Status_id = "Label_4431053#980928013011"
    Application_id = "Label_6204160254045272793"
    Joblist_id = "Label_6555342805228748060"
    
    try:
        try: 
            job_json = getGPT(email_text, subject, category)  # Get the JSON string from GPT-3
            # Removing the extraneous `json` and backticks
            clean_json = job_json.replace("json", "").strip().strip("`")
            data = json.loads(clean_json)  # Convert the JSON string to a dictionary   
        except Exception as error:
            print(f"ERROR occured in getGPT: {error}")
            return
        
        if (data.get("JobList") or "No") == "Yes":
            print("This email is a job listing")
            add_job(data, published_date)  # Add the job to Notion
            moveEmailToFolder(email_id, Joblist_id, service)

        elif ((data.get("Application") or "No") == "Yes") or (data.get("Update") or "No") == "Yes":
            print("This email is a application/status update")
            add_application(data, published_date)  # Add the application to Notion
            if (data.get("Update") or "No") == "Yes":
                moveEmailToFolder(email_id, Status_id, service) # Move email to Update folder
            else:
                moveEmailToFolder(email_id, Application_id, service) #Move email to Application folder
    
    except Exception as error:
        print(f"An error occurred in validEmail function: {error}")
        return
