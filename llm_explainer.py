import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Make sure it's set in the .env file.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def generate_explanation(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in detecting fake news."},
            {"role": "user", "content": f"Explain why the following news might be fake:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content.strip()
