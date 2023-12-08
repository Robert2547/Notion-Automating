from datetime import datetime, timezone
import os
from dotenv import load_dotenv

from notionDB import create_page, get_pages, update_page, delete_page

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
        "Company": {"type": "title", "title": [{"text": {"content": "Test Company"}}]},
        "Role": {"type": "title", "title": [{"text": {"content": "Test Role"}}]},
        "Location": {"type": "title", "title": [{"text": {"content": "Test Location"}}]},
        "URL": {"type": "url", "url": "https://www.notion.so/"},
        "Date": {"type": "date", "date": {"start": published_date, "end": None}},
    }

    create_page(data)

    pages = get_pages()

    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        company = props["Company"]["title"][0]["text"]["content"]
        status = props["Status"]["status"]["name"]
        published = props["Date"]["date"]["start"]
        published = datetime.fromisoformat(published)
        print(f"{page_id} - {company} - {status} - {published} \n\n")


if __name__ == "__main__":
    main()
