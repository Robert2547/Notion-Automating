import csv, re, io
from library.gmail import readEmail, extractEmail
import pandas as pd


def load_csv(service):

    Status_id = "Label_4431053980928013011"
    Application_id = "Label_6204160254045272793"
    Joblist_id = "Label_6555342805228748060"

    # Create a DataFrame for each category
    status_df = save_cvs(Status_id, "status", service)

    application_df = save_cvs(Application_id, "application", service)

    # joblist_df = save_cvs(Joblist_id, "joblist", service)

    # linkedin = reform_linkedin_dataset("models/dataset/linkedin_job.csv") # Reform LinkedIn dataset
    # joblist_df = pd.concat([joblist_df, linkedin], ignore_index=True) # Combine LinkedIn dataset with joblist dataset
    # joblist_df['Email Content'] = joblist_df['Email Content'].apply(clean_text) # Clean dataset
    # joblist_df.to_csv("models/dataset/joblist.csv", index=False) # Save dataset to CSV file

    joblist_df = pd.read_csv("models/dataset/joblist.csv")  # Load dataset from CSV file

    # Combine the datasets
    all_emails = pd.concat([status_df, application_df, joblist_df], ignore_index=True)

    # Save the combined dataset to a CSV file
    all_emails.to_csv("models/combined_emails.csv", index=False)


def save_cvs(label_ids, category, service):
    messages = []
    try:
        # Initialize request for messages
        request = service.users().messages().list(userId="me", labelIds=label_ids)

        # Loop to get all messages
        while request is not None:
            response = request.execute()
            messages.extend(response.get("messages", []))

            # Get the next page token and set up the next request, if there is a next page
            request = (
                service.users()
                .messages()
                .list_next(previous_request=request, previous_response=response)
            )

    except Exception as e:
        print(f"Error fetching messages: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of API call failure

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Category", "Subject", "Email Content"])

    for message in messages:
        try:
            message_id = message["id"]
            # Get the message_id and subject using readEmail
            _, subject = readEmail(message_id, service)
            email_content = extractEmail(message_id, service)
            email_content = clean_text(
                email_content
            )  # Assuming this is a function that cleans the email content

            # Writing the row to CSV
            writer.writerow([category, subject, email_content])
        except Exception as e:
            print(f"Error processing message {message_id}: {e}")

    output.seek(0)
    df = pd.read_csv(output)
    return df


def reform_linkedin_dataset(linkedin_file_path):
    """
    Reform a LinkedIn job postings dataset to match an existing structure with
    attributes: Category, Subject, From, Email Content. This function also filter job titles,
    and clean the text from emojis and ASCII characters.

    Parameters:
    - linkedin_file_path: str, the file path to the LinkedIn job postings CSV, dataset can be found in Kaggle.

    Returns:
    - New DataFrame with the reformed LinkedIn job postings dataset.
    """
    # Load the LinkedIn job postings dataset
    linkedin_jobs = pd.read_csv(linkedin_file_path, error_bad_lines=False)

    # Create a new DataFrame with the structure of the existing dataset
    reformed_dataset = pd.DataFrame()

    # Combine job title for 'Subject'
    reformed_dataset["Subject"] = linkedin_jobs["title"].astype(str)

    # Combine relevant fields for 'Email Content'
    reformed_dataset["Email Content"] = (
        linkedin_jobs["description"].astype(str)
        + " Location: "
        + linkedin_jobs["location"].fillna("").astype(str)
        + " Type: "
        + linkedin_jobs["formatted_work_type"].fillna("").astype(str)
        + " Apply at: "
        + linkedin_jobs["application_url"].fillna("").astype(str)
    )

    # Clean text from emojis and non-ASCII characters
    reformed_dataset["Email Content"] = reformed_dataset["Email Content"].apply(
        lambda x: re.sub(r"[^\x00-\x7F]+", " ", x)
    )

    # Assign the 'Category' and place it as the first column
    reformed_dataset["Category"] = "joblist"

    # Reorder columns to match the specified structure
    reformed_dataset = reformed_dataset[["Category", "Subject", "Email Content"]]

    # Filter for Software Engineer or Developer jobs
    filtered_jobs = reformed_dataset[
        reformed_dataset["Subject"].str.contains(
            "Software Engineer|Developer", case=False, na=False
        )
    ]

    return filtered_jobs


def clean_text(text):
    """
    Remove emojis, ASCII characters, and other non-essential information from the text.
    """
    # Decode using 'utf-8' and replace undecodable characters
    text = text.encode("utf-8", errors="replace").decode("utf-8")

    # Remove emojis and special symbols
    clean = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Remove extra whitespaces
    clean = " ".join(clean.split())
    return clean
