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

    messages = [
        {"role": "system", "content": "Jesteś pomocnym chatbotem."}
    ]

    while True:
        user_input = input("Zadaj pytanie, ewentualnie doprecyzuj lub quit: ")
        if user_input.lower() == "quit":
            print("Wracam do wyboru modelu.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.responses.create(
            model=user_ml,
            input=messages
        )

        assistant_reply = response.output_text
        messages.append({"role": "assistant", "content": assistant_reply})

        #print(messages)

        print(assistant_reply)


