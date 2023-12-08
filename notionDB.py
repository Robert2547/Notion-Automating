import requests, os

NOTION_KEY = os.environ.get("NOTION_KEY")
DATABASE_ID = os.environ.get("DATABASE_ID")

headers = {
    "Authorization": "Bearer " + NOTION_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.json())
    return res


def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    import json

    with open("db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data.get("results", [])

    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        if "results" in data:
            results.extend(data["results"])

    return results
