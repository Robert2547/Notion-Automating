from inbox import readEmail, authenticate_gmail, extractEmail
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
            .list(userId="me", includeSpamTrash=False)
            .execute()
        )

        i = 0
        for message in userId["messages"]:  # Loop through all messages
            i += 1
            if i == 8:
                break
            message_id = message["id"]  # Get the id of each message
            try:
                result = readEmail(
                    message_id, service
                )  # Store message id if it is important

                if result is not None:  # If the email is important, append it to the list
                    email_text = extractEmail(result, service) # Extract email text
                    print("\nEmail text:")
                    print(email_text)
                    validEmail(email_text) # Check if email is a job listing, status update or neither

                text = """Your job alert for software engineer intern in United States
        
6 new jobs match your preferences.  
          
Software Engineer Intern ( Remote )
RadicalX
San Francisco, CA
1 school alum
Apply with resume & profile
View job: https://www.linkedin.com/comm/jobs/view/3777830739/?trackingId=LiuOqbxovmbhC4yxo5tO%2BQ%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern
Lifetime Omics
Florida, United States
Apply with resume & profile
View job: https://www.linkedin.com/comm/jobs/view/3778155478/?trackingId=MymNzRZdCIiwh5xA%2BOGTHg%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern
Q2
Austin, TX
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3735119449/?trackingId=qwwgNS9jRigqF1Q4gTmjvw%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern D (Palm Bay, FL)
L3Harris Technologies
Palm Bay, FL
1 connection
View job: https://www.linkedin.com/comm/jobs/view/3716393706/?trackingId=nXe1%2BfJCRTtHvxQFsvdYLQ%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern, Cloud App
CNH Industrial
Oak Brook, IL
This company is actively hiring
Apply with resume & profile
View job: https://www.linkedin.com/comm/jobs/view/3715379860/?trackingId=94qXqwEAIVidz8hY7RJgtQ%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern, Cloud App
CNH Industrial
Oak Brook, IL
This company is actively hiring
Apply with resume & profile
View job: https://www.linkedin.com/comm/jobs/view/3715384332/?trackingId=dbSnJYSoJ5aMfjnlEYjV2A%3D%3D&refId=ByteString%28length%3D16%2Cbytes%3D34ea519d...6bd2922b%29&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job_card-0-view_job&trkEmail=eml-email_job_alert_digest_01-job_card-0-view_job-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

---------------------------------------------------------
  
See all jobs on LinkedIn:  https://www.linkedin.com/comm/jobs/search?geoId=103644278&f_TPR=a1702172867-&savedSearchId=1738265147&origin=JOB_ALERT_EMAIL&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job~alert-0-see~all~jobs~text&trkEmail=eml-email_job_alert_digest_01-job~alert-0-see~all~jobs~text-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D


See jobs where you’re a top applicant
https://www.linkedin.com/comm/premium/products/?utype=job&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-job~alert-0-premium~upsell~text&trkEmail=eml-email_job_alert_digest_01-job~alert-0-premium~upsell~text-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D
  

----------------------------------------

This email was intended for Joseph Benno (Computer Science @ UCF)
Learn why we included this: https://www.linkedin.com/help/linkedin/answer/4788?lang=en&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-SecurityHelp-0-textfooterglimmer&trkEmail=eml-email_job_alert_digest_01-SecurityHelp-0-textfooterglimmer-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D
You are receiving Job Alert emails.
Manage your job alerts:  https://www.linkedin.com/comm/jobs/alerts?lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-null-0-null&trkEmail=eml-email_job_alert_digest_01-null-0-null-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D 
Unsubscribe: https://www.linkedin.com/comm/jobs/alerts?lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-unsubscribe-0-textfooterglimmer&trkEmail=eml-email_job_alert_digest_01-unsubscribe-0-textfooterglimmer-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&loid=AQEtTG2qVjtqdgAAAYxWjzVAC7TRgBcTzjoFqmZjnaTXB7Xci1G0bm2JZeFf_Whm21uKOKG2RBFTuRJm3rUHu0YapjupvWdhmYX-YbVw5mQGvZhy4CFY7XOK5fyByMTr
Help: https://www.linkedin.com/help/linkedin/answer/67?lang=en&lipi=urn%3Ali%3Apage%3Aemail_email_job_alert_digest_01%3BkUB211dhTaupAn%2FzYdUi%2Bg%3D%3D&midToken=AQGPWHouMa64Xw&midSig=3pgKWbS6QHWb01&trk=eml-email_job_alert_digest_01-help-0-textfooterglimmer&trkEmail=eml-email_job_alert_digest_01-help-0-textfooterglimmer-null-iu95fh~lq097wlk~cu-null-null&eid=iu95fh-lq097wlk-cu&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjY4YWM3ZDI0NjljYWU4NjZiN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTRkNmM4ZDI3ZTliZDRjNjE0YTlkZWI0NjhmNmZjNGE3MzAwYmQ5MDExODdlMjBlLDEsMQ%3D%3D

© 2023 LinkedIn Corporation, 1zwnj000 West Maude Avenue, Sunnyvale, CA 94085.
LinkedIn and the LinkedIn logo are registered trademarks of LinkedIn."""

            except Exception as error:
                print(f"An error occurred: {error}")



    except Exception as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
# [END gmail_quickstart]
