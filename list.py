from datetime import datetime, timezone
import os
from dotenv import load_dotenv
from notion_api import create_page, get_pages, update_page, delete_page

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


def main():
    published_date = datetime.now().astimezone(timezone.utc).isoformat()

    data = {
        "Company": {"title": [{"text": {"content": "Test"}}]},
        "Role": {"rich_text": [{"text": {"content": "Test"}}]},
        "Location": {"rich_text": [{"text": {"content": "Test"}}]},
        "Date": {"date": {"start": published_date}},
        "URL": {"url": "https://www.notion.so/"},
    }

    create_page(data, DATABASE_ID, headers)


if __name__ == "__main__":
    main()
