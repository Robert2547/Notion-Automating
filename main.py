from library.gmail import readEmail, authenticate_gmail, extractEmail, removeLabelFromEmail
from library.validEmail import validEmail
from models.model  import model_main
from models.csv import load_csv
from joblib import load


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

        moveFolder =  0 # 1 = Application, 2 = Status, 3 = Joblist, 0 = Neither

        # Load saved model and vectorizer
        model = load("email_classifier_model.joblib")
        vectorizer = load("vectorizer.joblib")

        for message in userId.get("messages", []):  # Loop through all messages
            message_id = message["id"]  # Get the id of each message
            try:
                email_id, subject = readEmail(message_id, service)  # Store email id and subject
                if email_id is not None: # Check if email is not empty
                    try:
                        email_text = extractEmail(email_id, service) # Extract email text
                    except Exception as error:
                        print(f"An error occurred while trying to extract email: {error}")
                        print(f"Email id: {email_id}, Subject: {subject}")
                        continue

                    email_features = vectorizer.transform([email_text]) # Vectorize email content
                    prediction = model.predict(email_features)
                    category = prediction[0]
                    print(f"The email is categorized as: {category}")
                    
                    validEmail(email_text, subject, category, service, email_id) # Check if email is a job listing, status update or neither 

                    removeLabelFromEmail(service, email_id, "CATEGORY_UPDATES")

            except Exception as error:
                print(f"An error occurred while trying to read email: {error}")

    except Exception as error:
        # TODO
        print(f"An error occurred in main: {error}")


if __name__ == "__main__":
    main()
# [END gmail_quickstart]
