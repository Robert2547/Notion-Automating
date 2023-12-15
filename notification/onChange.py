from notion_client import Client
import time


def send_notification_on_change(token, database_id, notification_page_id):
    notion = Client(auth=token)
    last_checked_time = time.time()

    while True:
        # Check for updates in the database
        response = notion.databases.query(database_id)
        current_time = time.time()

        if response and response["last_edited_time"] > last_checked_time:
            # Change detected, add a notification in another Notion page
            notion.pages.create(
                parent={"page_id": notification_page_id},
                properties={"title": [{"text": {"content": "Database Updated"}}]},
                children=[
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "The database has been updated."
                                    },
                                }
                            ]
                        },
                    }
                ],
            )

            print("Notification sent on Notion.")
            last_checked_time = current_time

        time.sleep(60)  # Check every minute
