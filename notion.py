from datetime import datetime, timezone
from notionDB import create_page, get_pages, update_page, delete_page


def main():
    published_date = datetime.now().astimezone(timezone.utc).isoformat()

    data = {
        "Company": {"type": "title", "title": [{"text": {"content": "Test Company"}}]},
        "Status": {"type": "status", "status": {"name": "Applied"}},
        "Date": {"type": "date", "date": {"start": published_date, "end": None}},
        "Position": {"type": "multi_select", "multi_select": [{"name": "Software Engineer Intern"}]},
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
