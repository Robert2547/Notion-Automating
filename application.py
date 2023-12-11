from datetime import datetime, timezone
from notion_api import create_page, get_pages, update_page, delete_page
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
NOTION_KEY = os.getenv("NOTION_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def add_application(data, published_date):

    # Loop through each job in the JSON data
    for job in data["Job"]:
        print("\n\nJob:", job)
        # Extract each field
        company = job.get("Company", "N/A")
        status = job.get("Status", "N/A")
        role = "Software Engineer Intern"


        notion_format = {
        "Company": {"type": "title", "title": [{"text": {"content": company}}]},
        "Status": {"type": "status", "status": {"name": status}},
        "Date": {"type": "date", "date": {"start": published_date, "end": None}},
        "Position": {
            "type": "multi_select",
            "multi_select": [{"name": role}],
        },
    }

        create_page(notion_format, DATABASE_ID, headers)

   

