from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
    model="openai/gpt-4.1-nano",
    messages=[{"role": "user", "content": "Co jest stolica polski?"}])

print(completion.choices[0].message.content)
