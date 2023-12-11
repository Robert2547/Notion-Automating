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


def getGPT(email):
    stream = client.chat.completions.create( 
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": """Pretend you are a consultants at analyzing email. You are given a email about software, determine whether this email is about new job posting, if so format the response in JSON format, such as: 
"Job": [{
     "Company": "string"
     "Role": "string"
     "Location": "string"
    "URL": "string"
}]""",
            },
            {
                "role": "user",
                "content": email,
            },
        ], stream=True, # Return a stream of results
    )
    #for chunk in stream: # Iterate over the chunks of the stream
        #if chunk.choices[0].delta.content is not None: # Check if the model has generated a response
            #print(chunk.choices[0].delta.content, end="") # Print the response
    return stream
