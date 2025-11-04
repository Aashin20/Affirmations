from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def get_affirmations(mood: str):
    prompt = f"Please generate one powerful affirmation for someone who is feeling {mood}. Only return the affimation with no formatting."

    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"
    
