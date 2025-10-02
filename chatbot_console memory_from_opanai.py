from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def choose_model():
    print("Hej, jestem Twoim Chatbotem!")
    return input("Wybierz model gpt-4.1-nano, gpt-5 albo quit: ").strip()

def chat_with_model(model):
    conv_id = None
    while True:
        user_input = input("Zadaj pytanie, ewentualnie doprecyzuj lub quit: ").strip()
        if user_input.lower() == "quit":
            print("Wracam do wyboru modelu.")
            break

        kwargs = {
            "model" : model,
            "input" : [{"role": "user",
                        "content" : user_input}],
        }
        
        if conv_id is not None:
            kwargs["previous_response_id"] = conv_id

        response = client.responses.create(**kwargs)
        conv_id = response.id
        
        print(response.output_text)


def main():
    while True:
        model = choose_model()
        if model.lower() == "quit":
            print("Kończę zabawę.")
            break
        chat_with_model(model)

if __name__ == "__main__":
    main()
