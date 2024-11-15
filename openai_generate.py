import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

def llm_generate_response(title: str, body: str):
    user_prompt = f'''Please research the company with the following website. Title: {title}. Body {body}. 
                      Provide a structured summary with the following sections:

                     <INDUSTRY>
                        [Briefly describe the industry this company operates in]
                     </INDUSTRY>

                     <PRODUCTS OR SERVICES>
                        [Summarize the main products or services the company offers]
                     </PRODUCTS OR SERVICES>

                     <TARGET AUDIENCE> 
                        [Identify the primary target customers or markets for the company]
                     </TARGET AUDIENCE> 

                     <MARKET POSITION> 
                        [Describe the company’s position in the market (e.g., market leader, emerging player)].
                     </MARKET POSITION> 
                    
                     <RECENT NEW OR EVENTS>
                        [Include any recent news, significant events, or milestones relevant to the company].
                     </RECENT NEW OR EVENTS>
                    
                     Aim to provide actionable insights that would help a sales team preparing to reach out to this prospect.
                    
                     Output as:
                     [html code]
                    '''

    prompt = [
        {
            'role': 'system',
            'content': 'You are an AI assistant specializing in prospect research for a sales team. Your task is to analyze a given company website and produce a concise, structured summary of the company for the sales team. The output should be in html code, just with a div with h and p elements.'
        },
        {
            'role': 'user',
            'content': user_prompt
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt,
    )

    return response.choices[0].message.content