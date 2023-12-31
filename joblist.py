import os, requests
from dotenv import load_dotenv
from library.notion import create_page, get_pages

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
#Joblist notion key
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


def add_job(data, published_date):
    # Loop through each job in the JSON data
    for job in data["Jobs"]:

        if exists(job):
            continue # Skip if the job already exists in the joblist notion database

        company = job.get("Company", "N/A")
        role = job.get("Role", "N/A")
        location = job.get("Location", "N/A")
        url = job.get("URL", "N/A")

        notion_format = {  # Format the data for Notion
            "Company": {"title": [{"text": {"content": company}}]},
            "Role": {"rich_text": [{"text": {"content": role}}]},
            "Location": {"rich_text": [{"text": {"content": location}}]},
            "Date": {"date": {"start": published_date}},
            "URL": {"url": url},
        }
        create_page(notion_format, DATABASE_ID, headers)  # Create a new page in Notion
        
    return 3 # Move to Trash folder

# Check if the job already exists in the joblist notion database
def exists(job):
    joblist = get_pages(headers, DATABASE_ID)  # Get all pages in the joblist notion database
    for page in joblist:
        if (page["properties"]["Company"]["title"][0]["text"]["content"] == job.get("Company", "N/A")) and (page["properties"]["Role"]["rich_text"][0]["text"]["content"] == job.get("Role", "N/A")):
            return True
    return False
