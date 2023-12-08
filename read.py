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