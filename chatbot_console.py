from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

while True:
    print("Hej, jestem Twoim Chatbotem!")
    user_ml = input("Wybierz model gpt-4.1-nano, gpt-5 albo quit: ")

    if user_ml.lower() == "quit":
        print("Kończę zabawę.")
        break

    user_q = input("Zadaj pytanie: ")

    response = client.responses.create(
        model=user_ml,
        input=user_q
    )

    print(response.output_text)
