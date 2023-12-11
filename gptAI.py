from dotenv import load_dotenv
import os, json
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


def getGPT(email):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": """Pretend you are a consultants at analyzing email. You are given a email about software, determine whether this email is about new job posting, if so format the response in JSON format, such as: 
{
     Company:
     Role:
     Location:
    URL:
} if its anything else return the response in following JSON format and nothing else:
{
    Joblist: "No"
}
""",
            },
            {
                "role": "user",
                "content": email,
            },
        ],
    )

    # Extract the response
    generated_text = response.choices[0].message.content

    return generated_text
