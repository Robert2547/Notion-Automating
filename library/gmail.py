import base64
import email, re
import os.path

from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


# Function to authenticate and build the Gmail service
def authenticate_gmail():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# Function to extract the email text
def extractEmail(message_id, service):
    try:
        # Get the message from its ID
        message = service.users().messages().get(userId='me', id=message_id, format='raw').execute()

        # Decode the email
        msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_str)

        # Extract and clean content
        text = ""
        if mime_msg.is_multipart():
            for part in mime_msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain' or content_type == 'text/html':
                    part_payload = part.get_payload(decode=True).decode()
                    if content_type == 'text/html':
                        soup = BeautifulSoup(part_payload, 'html.parser')
                        for script_or_style in soup(["script", "style"]):
                            script_or_style.decompose()
                        clean_text = soup.get_text()
                        text += clean_text + "\n"
                    else:
                        text += part_payload + "\n"
        else:
            content_type = mime_msg.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                payload = mime_msg.get_payload(decode=True).decode()
                if content_type == 'text/html':
                    soup = BeautifulSoup(payload, 'html.parser')
                    for script_or_style in soup(["script", "style"]):
                        script_or_style.decompose()
                    text = soup.get_text()
                else:
                    text = payload

        # Remove URLs
        text_no_urls = re.sub(r'http\S+', '', text)

        # Remove excessive whitespaces
        cleaned_text = re.sub(r'\s+', ' ', text_no_urls).strip()
        return cleaned_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to read the email
def readEmail(message_id, service):
    message_from = message_date = subject = ""
    message = (  # Get the message object
        service.users().messages().get(userId="me", id=message_id).execute()
    )

    # Loop through all headers and collect the sender, date, and subject
    for header in message["payload"]["headers"]:
        if header["name"] == "From":
            message_from = header["value"]
            # print(message_from)
        elif header["name"] == "Date":
            message_date = header["value"]
            # print(message_date)
        elif header["name"] == "Subject":
            subject = header["value"]
            # print(subject)
            break  # break the loop when get the subject

    return message_id, subject


# Function to move the email to a folder
def moveEmailToFolder(message_id, folder_id, service):
    try:
        # The body of the request specifies adding the folder's label ID
        # and removing the 'INBOX' label to simulate moving the email.
        body = {"addLabelIds": [folder_id], "removeLabelIds": ["INBOX"]}

        message = (
            service.users()
            .messages()
            .modify(userId="me", id=message_id, body=body)
            .execute()
        )
        return message
    except Exception as error:
        print(f"An error occurred while moving the email: {error}")
        return None


# Function to list all the labels id
def list_labels(service):
    try:
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")
        for label in labels:
            print(f"Label Name: {label['name']}, Label Id: {label['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")


# Function to remove label from email
def removeLabelFromEmail(service, message_id, label_ids):
    service.users().messages().modify(
        userId="me", id=message_id, body={"removeLabelIds": [label_ids]}
    ).execute()
