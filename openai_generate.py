import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

def llm_generate_response(title: str, body: str):
    prompt = [
        {
            'role': 'system',
            'content': 'You are an AI assistant specializing in prospect research for a sales team. Your task is to analyze a given company website and produce a concise, structured summary of the company for the sales team.'
        },
        {
            'role': 'user',
            'content': f'''Please research the company with the following website. Title: {title}. Body {body}. Provide a structured summary with the following sections:

                - Industry: [Briefly describe the industry this company operates in].
                - Products/Services: [Summarize the main products or services the company offers].
                - Target Audience: [Identify the primary target customers or markets for the company].
                - Market Position: [Describe the company’s position in the market (e.g., market leader, emerging player)].
                - Recent News/Events: [Include any recent news, significant events, or milestones relevant to the company].

                 Aim to provide actionable insights that would help a sales team preparing to reach out to this prospect.
            '''
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
    )

    return response.choices[0].message.content