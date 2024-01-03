import csv
from library.gmail import readEmail, extractEmail
import pandas as pd



#This function saves the email data into a csv file
def save_cvs(label_ids, file_name, service):
    # List all messages
    response = service.users().messages().list(userId='me', labelIds=label_ids).execute()
    messages = response.get('messages', [])

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category','Subject', 'Email Content'])
        print("Writing to csv file")

        for message in messages:
            message_id = message['id']
            message_id, subject = readEmail(message_id, service)
            email_content = extractEmail(message_id, service)

            writer.writerow(["status", subject, email_content])


def reform_linkedin_dataset(linkedin_file_path, output_file_path):
    """
    Reform a LinkedIn job postings dataset to match an existing structure with
    attributes: Category, Subject, From, Email Content.

    Parameters:
    - linkedin_file_path: str, the file path to the LinkedIn job postings CSV, dataset can be found in Kaggle.
    - output_file_path: str, the file path where the reformed CSV will be saved.

    Returns:
    - None, but writes a new CSV file to the specified output path.
    """
    # Load the LinkedIn job postings dataset
    linkedin_jobs = pd.read_csv(linkedin_file_path)

    # Create a new DataFrame with the structure of the existing dataset
    reformed_dataset = pd.DataFrame()

    # Assign the 'Category'
    reformed_dataset['Category'] = 'joblist'

    # Combine job title and company name for 'Subject'
    reformed_dataset['Subject'] = linkedin_jobs['title'] 

    # Combine relevant fields for 'Email Content'
    reformed_dataset['Email Content'] = linkedin_jobs['description'] + ' ' + \
                                        'Location: ' + linkedin_jobs['location'].fillna('') + ' ' + \
                                        'Type: ' + linkedin_jobs['formatted_work_type'].fillna('') + ' ' + \
                                        'Apply at: ' + linkedin_jobs['application_url'].fillna('')
                                        

    # Save the reformed dataset to a new CSV file
    reformed_dataset.to_csv(output_file_path, index=False)
    print(f"Reformed dataset saved to {output_file_path}")