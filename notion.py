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

    pages = get_pages()

    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        company = props["Company"]["title"][0]["text"]["content"]
        status = props["Status"]["select"]["name"]
        published = props["Published"]["date"]["start"]
        published = datetime.fromisoformat(published)


if __name__ == "__main__":
    main()
