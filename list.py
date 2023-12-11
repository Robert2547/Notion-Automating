from datetime import datetime, timezone
import os, json, requests
from dotenv import load_dotenv
from gptAI import getGPT
from notion_api import create_page

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
NOTION_KEY = os.getenv("SWE_KEY")
DATABASE_ID = os.getenv("SWE_DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def shorten_url(url):
    api_url = "http://www.linkedin.com"
    params = {"url": url}
    response = requests.get(api_url, params=params)
    return response.text


def main():
    job_json = getGPT(

        """ Top job picks for you: https://www.linkedin.com/comm/jobs/collections/recommended?origin=JYMBII_EMAIL&lgCta=eml-jymbii-bottom-see-all-jobs&lgTemp=jobs_jymbii_digest&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-null-0-null&trkEmail=eml-jobs_jymbii_digest-null-0-null-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D
  
          
Internship, Software Engineer
VSP Vision Care
United States
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3780846169/?trackingId=7Cqsu2WLT%2BSmxsHYYLqMaQ%3D%3D&refId=KjxFguxmRrWhAkBJ6eeKrA%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Intern I - Software Development Engineering
Dexcom
United States
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3778795712/?trackingId=io5HID8hQv6wXbnCV%2FjQGQ%3D%3D&refId=52TnKUVbQmulNK0PaH%2B2BA%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Artificial Intelligence Intern
Cerebrone.ai
Charlotte
High skills match
Apply with resume & profile
View job: https://www.linkedin.com/comm/jobs/view/3782356402/?trackingId=LjOSJvicTqKSzaxJIXGIAA%3D%3D&refId=LZdw3vhkT12%2F4NHuwpF33Q%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Intern
Intel Corporation
Arizona
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3779843601/?trackingId=O3XvgDJXRNSO3AWdYx1aRQ%3D%3D&refId=MiqXncWnQ%2FyIYyjOZOlBXA%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern (CEC)
Epsilon C5I
Largo
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3726717610/?trackingId=LI4AGl0tS8Sdpv7CRoTSMw%3D%3D&refId=e7UsdcKISumFU%2FgguXZN%2Bg%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
          
Software Engineer Intern - Perks (Core Product)
Discord
San Francisco
This company is actively hiring
View job: https://www.linkedin.com/comm/jobs/view/3762360753/?trackingId=Qy842qO1RCqEfmF15I3pMA%3D%3D&refId=wj0XBzFiSfKLlqi8BYXflw%3D%3D&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-job_card-0-view_job&trkEmail=eml-jobs_jymbii_digest-job_card-0-view_job-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D

---------------------------------------------------------
  
See all jobs https://www.linkedin.com/comm/jobs/collections/recommended?origin=JYMBII_EMAIL&lgCta=eml-jymbii-bottom-see-all-jobs&lgTemp=jobs_jymbii_digest&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-null-0-null&trkEmail=eml-jobs_jymbii_digest-null-0-null-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D
See jobs where you’re a top applicant
https://www.linkedin.com/comm/premium/products/?utype=job&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-jymbii-0-premium~upsell~text&trkEmail=eml-jobs_jymbii_digest-jymbii-0-premium~upsell~text-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D
  


----------------------------------------

This email was intended for Joseph Benno (Computer Science @ UCF)
Learn why we included this: https://www.linkedin.com/help/linkedin/answer/4788?lang=en&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-SecurityHelp-0-textfooterglimmer&trkEmail=eml-jobs_jymbii_digest-SecurityHelp-0-textfooterglimmer-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D
You are receiving Jobs You Might Be Interested In emails.
 https://www.linkedin.com/comm/jobs/alerts?lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-null-0-null&trkEmail=eml-jobs_jymbii_digest-null-0-null-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D 
Unsubscribe: https://www.linkedin.com/comm/psettings/email-unsubscribe?lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-unsubscribe-0-textfooterglimmer&trkEmail=eml-jobs_jymbii_digest-unsubscribe-0-textfooterglimmer-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&loid=AQEvgaYeVD1dqgAAAYxKtwImNbwmn6qTzaoOlCAm9wDYF6tkxccEFxjhr9A8wwcO0r1w8ONTBAAUH1Un4ieJZUstnT0S-xlEN_zsam5iQos
Help: https://www.linkedin.com/help/linkedin/answer/67?lang=en&lipi=urn%3Ali%3Apage%3Aemail_jobs_jymbii_digest%3BoJm3PurJSSK13UoFrYB2Ug%3D%3D&midToken=AQGPWHouMa64Xw&midSig=1VePZ4Pl4XSX01&trk=eml-jobs_jymbii_digest-help-0-textfooterglimmer&trkEmail=eml-jobs_jymbii_digest-help-0-textfooterglimmer-null-iu95fh~lpwyjlff~v1-null-null&eid=iu95fh-lpwyjlff-v1&otpToken=MTMwNDFkZTkxMDJlY2ZjMWJjMjcwZmViNDExZWU1YjQ4OWNlZDU0NDlmYTY4YTYzN2JjZjA2NmE0YjUzNTRmM2YxZGNkMmU5NTFkNmVkZTI1MGYyYWI4NTM2NTc3MmExZWE0MDhmN2RmMzEwMjE3OTQ2NGU0M2NhLDEsMQ%3D%3D """
    )
    
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
   
    try:
         # Removing the extraneous `json` and backticks
        clean_json = job_json.replace('json', '').strip().strip('`')

        data = json.loads(clean_json) # Convert the JSON string to a dictionary
        # Loop through each job in the JSON data
        for job in data["Job"]:
            print("\n\nJob:", job)
            # Extract each field
            company = job.get("Company", "N/A")
            role = job.get("Role", "N/A")
            location = job.get("Location", "N/A")
            url = job.get("URL", "N/A")
            
            notion_format = { # Format the data for Notion
            "Company": {"title": [{"text": {"content": company}}]},
            "Role": {"rich_text": [{"text": {"content": role}}]},
            "Location": {"rich_text": [{"text": {"content": location}}]},
            "Date": {"date": {"start": published_date}},
            "URL": {"url": url},
            }

            create_page(notion_format, DATABASE_ID, headers) # Create a new page in Notion
    
            print ("Job added to Notion")
    except Exception as e:
        print("Error: ", e)
        return


        

if __name__ == "__main__":
    main()
