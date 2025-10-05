import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

messages = [{"role": "system", "content": "Jesteś pomocnym chatbotem."}]

while True:
    user_input = input("Ty: ")

    if user_input.lower() == "quit":
        print("Do zobaczenia!")
        break

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages= messages
    )

    messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    print(completion.choices[0].message.content)




