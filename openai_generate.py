import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

def llm_generate_response(title: str, body: str):
    prompt = [{'role': 'system', 'content': 'You are an AI HR assistant which helps to select the best candidated to the given job.'},
              {'role': 'user',   'content': prompt}]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
    )

    return response.choices[0].message.content