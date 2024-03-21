from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv(".env")

# Get your API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key:
    # Initialize OpenAI client with the API key
    client = OpenAI(api_key=api_key)
else:
    print("API key not found in environment variables.")


def getGPT(email, subject, category):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """  PPretend you are a consultants at analyzing email. Given a email content, subject and help from my ML output, categorize the following email into JobList, Application UPDATE, or NEW Application. If the following contain information about new job list use this JSON format: "JobList": "Yes",
{  Jobs:[   
     "Company":
     "Role":
     "Location":
    "URL":
]} 

Else if it about NEW application use the following JSON format:
"Application": "Yes",
{
    "Company":
    "Status": "Applied"
    "Role": 
}

Else if it about application UPDATE use the following JSON format:
“Update”: “Yes”,
{
	"Company":
    	"Status": "Rejected"/"Interview"/"Online Assignment"
   	 "Role": 
}
Else if its anything else return the response in following JSON format and nothing else:
{
    "Joblist":  "No"
    "Application": "No"
} 

""",
            },
            {
                "role": "user",
                "content": "Subject: " + subject + "\nEmail: " + email + "ML Category: " + category,
            },
        ],
        temperature=0.9,
    )

    # Extract the response
    generated_text = response.choices[0].message.content

    return generated_text
