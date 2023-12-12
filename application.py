from notion_api import create_page, get_pages, update_page, delete_page
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
STATUS_KEY = os.getenv("NOTION_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")


JOBLIST_KEY = os.getenv("SWE_KEY")
JOBDB_KEY = os.getenv("SWE_DATABASE_ID")




headers_status = {
    "Authorization": f"Bearer {STATUS_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

headers_application = {
    "Authorization": f"Bearer {JOBLIST_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def add_application(data, published_date):
    # Extract each field
    company = data.get("Company", "N/A")
    status = data.get("Status", "N/A")
    role = data.get("Role", "N/A")

    print("\nCompany:", company)
    print("Status:", status)

    moveOption = 0

    try:
        page = get_pages(headers_status, DATABASE_ID)  # Get all pages in the database

        for pages in page:  # Loop through each page
            if ( pages["properties"]["Company"]["title"][0]["text"]["content"] == company ):  # If the company name already exists in the status notion database
                joblist_page = get_pages( headers_application, JOBDB_KEY )  # Get all pages in the joblist notion database

                for joblist_pages in joblist_page:  # Loop through each page

                    if (joblist_pages["properties"]["Company"]["title"][0]["text"]["content"] == company) and (joblist_pages["properties"]["Role"]["rich_text"][0]["text"]["content"] == role):
                        # If the company name and role already exists in the joblist notion database
                        # Move the page to the trash, update the status and move the email to trash
                        joblist_page_id = joblist_pages["id"]
                        print("Updating joblist...")
                        delete_page(joblist_page_id, headers_application)  # Move the page to the trash
                        print("Joblist updated successfully")
                        moveOption = 3 # Move to Trash folder
                        break
                         
                page_id = pages["id"]
                print("Updating status...")
                update_page( page_id, {"Status": {"name": status}}, headers_status)  # Update the status
                print("Status updated successfully")

                if moveOption != 3:
                    moveOption = 1 # Move to Status folder
                return moveOption  
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

    create_page(notion_format, DATABASE_ID, headers_status)
    print("Application added successfully")
    return 2 # Move to Application folder
