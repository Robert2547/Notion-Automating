import base64
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


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
        "@myworkday.com",
    ]

    # Check if any keyword is in the sender's email or subject
    for keyword in keywords:
        if keyword in email_from_lower or keyword in subject_lower:
            return True  # Return True if any keyword is found

    return False  # Return False if none of the keywords are found


# Function to extract the text from the email
def extractEmail(message_id, service):
    message = service.users().messages().get(userId='me', id=message_id).execute()
    message_payload = message["payload"]

    if "parts" in message_payload:  # Check if the message is multipart
        parts = message_payload["parts"]  # Get the parts of the message
        email_text = ""
        for part in parts:
            if part["mimeType"] == "text/plain":
                email_text += base64.urlsafe_b64decode(part["body"]["data"]).decode(
                    "utf-8"
                )  # Decode the text from base64
    else:  # If the message is not multipart, extract text directly from the body
        email_text = base64.urlsafe_b64decode(message_payload["body"]["data"]).decode(
            "utf-8"
        )
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
        #print(message_id)
        #print(message_from)
        #print(subject + "\n")
        return message_id
    return
