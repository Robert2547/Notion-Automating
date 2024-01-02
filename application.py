from library.notion import create_page, get_pages, update_page, delete_page
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
    role = data.get("Role", "Software Engineer Intern (default)")
    if len(role) < 5:
        role = "Software Engineer Intern (default)"
    

    print("\nCompany:", company)
    print("Status:", status)
    print("Role:", role)
    print("\n")

    moveOption = 0

    try:
        page = get_pages(headers_status, DATABASE_ID)  # Get all pages in the database

        for pages in page:  # Loop through each page
            if (pages["properties"]["Company"]["title"][0]["text"]["content"] == company):  # If the company name already exists in the status notion database
                joblist_page = get_pages( headers_application, JOBDB_KEY )  # Get all pages in the joblist notion database
                print("\nCompany already exists in the APPLICATION database!")
                for joblist_pages in joblist_page:  # Loop through each page
                    if (joblist_pages["properties"]["Company"]["title"][0]["text"]["content"] == company) and (joblist_pages["properties"]["Role"]["rich_text"][0]["text"]["content"] == role):
                        # If the company name and role already exists in the JOBLIST database
                        # Delete the page in JOBLIST database and update the status in APPLICATION database
                        print("\nCompany and role already exists in the JOBLIST database!")
                        joblist_page_id = joblist_pages["id"]
                        delete_page(joblist_page_id, headers_application)  # Move the page to the trash
                        print("Page has been deleted!\n")
                        break

                # If company already exists, but role does not exist, then add new page
                if(pages["properties"]["Position"]["rich_text"][0]["text"]["content"] != role):
                    print("Role does not exists in the APPLICATION database!")
                    break
                

                page_id = pages["id"]
                update_page( page_id, {"Status": {"status": {"name": status}}}, headers_status)  # Update the status
                return 2 # Move to Status folder  
        print("\nCompany does not exist in the application notion database!") 
    except Exception as error:
        print(f"An error occurre in add_application: {error}")
        return

    notion_format = {
        "Company": {"type": "title", "title": [{"text": {"content": company}}]},
        "Status": {"type": "status", "status": {"name": status}},
        "Date": {"type": "date", "date": {"start": published_date, "end": None}},
        "Position": {"rich_text": [{"text": {"content": role}}]},
    }
    res = create_page(notion_format, DATABASE_ID, headers_status)
    print("Application added successfully")

    return 1 # Move to Application folder
