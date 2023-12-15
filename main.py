from library.gmail import readEmail, authenticate_gmail, extractEmail, moveEmailToFolder
from validEmail import validEmail


def main():

    try:
        # Call the Gmail API
        service = authenticate_gmail()

        # Get message in user's mailbox
        # Contain message object: id, threadId, nextPageToken, resultSizeEstimate
        userId = (
            service.users()
            .messages()
            .list(userId="me", q="category:updates", includeSpamTrash=False)
            .execute()
        )

        moveFolder =  0 # 1 = Status, 2 = Joblist, 3 = Trash

        Status_id = "Label_4431053980928013011"
        Application_id = "Label_6204160254045272793"
        for message in userId.get("messages", []):  # Loop through all messages
            message_id = message["id"]  # Get the id of each message

            try:
                result_id = readEmail(message_id, service)  # Store message id if it is important

                if result_id is not None:  # If the email is important, append it to the list

                    email_text = extractEmail(result_id, service) # Extract email text
                    print("\nEmail text:")
                    print(email_text)
                    moveFolder = validEmail(email_text) # Check if email is a job listing, status update or neither

                    if moveFolder == 1:
                       print("Moving email to Application/Status folder")
                       moveEmailToFolder(result_id, Status_id, service) # Move email to Application/Status folder

                    elif moveFolder == 2:
                        print("Moving email to Joblist folder")
                        moveEmailToFolder(result_id, Application_id, service) # Move email to Joblist folder

                    elif moveFolder == 3:
                        print("Moving email to Trash folder")
                        moveEmailToFolder(result_id, "TRASH", service)
                    else:
                        print("Email is neither a job listing nor a application update")

            except Exception as error:
                print(f"An error occurred while trying to read email: {error}")

    except Exception as error:
        # TODO
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
# [END gmail_quickstart]
