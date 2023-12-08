from datetime import datetime, timezone
from notionDB import create_page, get_pages


def main():
    published_date = datetime.now().astimezone(timezone.utc).isoformat()

    data = {
        "Company": {"type": "title", "title": [{"text": {"content": "Test Company"}}]},
        "Status": {"type": "status", "status": {"name": "Done"}},
        "Date": {"type": "date", "date": {"start": published_date, "end": None}},
    }

    create_page(data)


if __name__ == "__main__":
    main()
