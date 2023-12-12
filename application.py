from notion_api import create_page, get_pages, update_page
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
    # Extract each field
    company = data.get("Company", "N/A")
    status = data.get("Status", "N/A")
    role = "Software Engineer Intern"

    print("\nCompany:", company)
    print("Status:", status)

    try:
        page = get_pages(headers, DATABASE_ID)  # Get all pages in the database
        for pages in page:  # Loop through each page
            if (
                pages["properties"]["Company"]["title"][0]["text"]["content"] == company
            ):  # If the company name already exists in the database
                page_id = pages["id"]
                print("Page ID:", page_id)
                print("Updating status...")
                update_page(page_id, {"Status": {"name": status}}, headers) # Update the status
                print("Status updated successfully")
                return 1 # Move to Status folder
    except Exception as error:
        print(f"An error occurred: {error}")
        return
    
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
    print("Application added successfully")
    return 2 # Move to Application folder
