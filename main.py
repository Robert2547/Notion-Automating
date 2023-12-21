from library.gmail import readEmail, authenticate_gmail, extractEmail, moveEmailToFolder, removeLabelFromEmail, list_labels
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

        moveFolder =  0 # 1 = Application, 2 = Status, 3 = Trash(Joblist)

        Status_id = "Label_4431053980928013011"
        Application_id = "Label_6204160254045272793"
        Joblist_id = "Label_6555342805228748060"
        
        for message in userId.get("messages", []):  # Loop through all messages
            message_id = message["id"]  # Get the id of each message
            try:
                result_id, subject = readEmail(message_id, service)  # Store message id if it is important
                if result_id is not None:  
                    email_text = extractEmail(result_id, service) # Extract email text
                    moveFolder = validEmail(email_text, subject) # Check if email is a job listing, status update or neither 

                    if moveFolder != 0: #Remove updates label
                        removeLabelFromEmail(service, result_id, "CATEGORY_UPDATES")

                    if moveFolder == 2: # Move status update email to status folder
                       print("Moving email to Status folder")
                       moveEmailToFolder(result_id, Status_id, service) 

                    elif moveFolder == 1: # Move new application email to application folder
                        print("Moving email to Application folder")
                        moveEmailToFolder(result_id, Application_id, service) 

                    elif moveFolder == 3: # Move joblist email to trash
                        print("Moving email to Trash folder")
                        moveEmailToFolder(result_id, Joblist_id, service)
                    else:
                        print("Email is neither a job listing nor a application update")

            except Exception as error:
                print(f"An error occurred while trying to read email: {error}")

    except Exception as error:
        # TODO
        print(f"An error occurred in main: {error}")


if __name__ == "__main__":
    main()
# [END gmail_quickstart]
