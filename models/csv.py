import csv
from library.gmail import readEmail, extractEmail



#This function saves the email data into a csv file
def save_cvs(label_ids, output_csv_file, service):
    # List all messages
    response = service.users().messages().list(userId='me', labelIds=label_ids).execute()
    messages = response.get('messages', [])

    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'From', 'Email Content'])
        print("Writing to csv file")

        for message in messages:
            message_id = message['id']
            message_id, subject, message_from = readEmail(message_id, service)
            email_content = extractEmail(message_id, service)

            writer.writerow([subject, message_from, email_content])
        print("Done writing to csv file")
