from inbox import readEmail, authenticate_gmail, extractEmail
from joblist import joblist


def main():
    try:
        # Call the Gmail API
        service = authenticate_gmail()

        # Get message in user's mailbox
        # Contain message object: id, threadId, nextPageToken, resultSizeEstimate
        userId = (
            service.users()
            .messages()
            .list(userId="me", includeSpamTrash=False)
            .execute()
        )

        validEmail = []  # List of emails subject about Software Engineering
        i = 0
        for message in userId["messages"]:  # Loop through all messages
            i += 1
            if i == 20:
                break
            message_id = message["id"]  # Get the id of each message
            try:
                result = readEmail(
                    message_id, service
                )  # Store message id if it is important

                if (
                    result is not None
                ):  # If the email is important, append it to the list
                    validEmail.append(result)
                    email_text = extractEmail(result, service) # Extract email text
                    joblist(email_text)  # Create a new page in Notion, if the email is about job listing
                    
            except:
                print(f"Error reading email with id: {message_id}")
                continue

    except Exception as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
# [END gmail_quickstart]
