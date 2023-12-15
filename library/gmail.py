import base64
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


# Function to check if the email is anything related to Software Engineering
def isImportant(email_from, subject):
    # Convert both the sender's email and subject to lowercase for case-insensitive matching
    email_from_lower = email_from.lower()
    subject_lower = subject.lower()

    # List of keywords to check for
    keywords = [
        "software",
        "intern",
        "internship",
        "software internship",
        "thank you for applying",
        "thank", "application", "apply"
    ]

    # Check if any keyword is in the sender's email or subject
    for keyword in keywords:
        if keyword in email_from_lower or keyword in subject_lower:
            return True  # Return True if any keyword is found

    return False  # Return False if none of the keywords are found


# Function to extract the text from the email
def extractEmail(message_id, service):
    message = service.users().messages().get(userId="me", id=message_id).execute()
    message_payload = message["payload"]

    if "parts" in message_payload:
        parts = message_payload["parts"]
        email_text = ""
        for part in parts:
            if part["mimeType"] == "text/html":  # Look for HTML content
                html_content = base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8")
                soup = BeautifulSoup(html_content, "html.parser")
                for p in soup.find_all('p'):  # Extract text from paragraph tags
                    email_text += p.get_text() + "\n"
    else:
        if message_payload["mimeType"] == "text/html":
            html_content = base64.urlsafe_b64decode(message_payload["body"]["data"]).decode("utf-8")
            soup = BeautifulSoup(html_content, "html.parser")
            email_text = "\n".join(p.get_text() for p in soup.find_all('p'))

    return email_text


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

    is_important = isImportant(message_from, subject)
    if is_important:
        return message_id
    return

#Function to move the email to a folder
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
        print(
            f"Message Id: {message['id']} moved to folder with Label Id: {folder_id}."
        )
        return message
    except Exception as error:
        print(f"An error occurred while moving the email: {error}")
        return None

#Function to list all the labels id
def list_labels(service):
    try:
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(f"Label Name: {label['name']}, Label Id: {label['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")