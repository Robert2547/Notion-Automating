from datetime import datetime, timezone
import os, json, requests
from dotenv import load_dotenv
from gptAI import getGPT
from notion_api import create_page

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
NOTION_KEY = os.getenv("SWE_KEY")
DATABASE_ID = os.getenv("SWE_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def shorten_url(url):
    api_url = "http://www.linkedin.com"
    params = {"url": url}
    response = requests.get(api_url, params=params)
    return response.text


def joblist(email_text):
    job_json = getGPT(email_text)
    
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
   
    try:
         # Removing the extraneous `json` and backticks
        clean_json = job_json.replace('json', '').strip().strip('`')

        data = json.loads(clean_json) # Convert the JSON string to a dictionary

        if data.get("Joblist", "No").lower() == "no": #This email is not about joblisting
            print("Not a job listing")
            return
        
        # Loop through each job in the JSON data
        for job in data["Job"]:
            print("\n\nJob:", job)
            # Extract each field
            company = job.get("Company", "N/A")
            role = job.get("Role", "N/A")
            location = job.get("Location", "N/A")
            url = job.get("URL", "N/A")
            
            notion_format = { # Format the data for Notion
            "Company": {"title": [{"text": {"content": company}}]},
            "Role": {"rich_text": [{"text": {"content": role}}]},
            "Location": {"rich_text": [{"text": {"content": location}}]},
            "Date": {"date": {"start": published_date}},
            "URL": {"url": url},
            }

            create_page(notion_format, DATABASE_ID, headers) # Create a new page in Notion
    
            print ("Job added to Notion")
    except Exception as e:
        print("Error: ", e)
        return
