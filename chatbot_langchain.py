from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(model="gpt-4.1-mini", model_provider="openai")

while True:
    user_input = input("Ty: ")
    if user_input.lower() in {"quit", "exit", "stop", "koniec"}:
        print("Zakończono rozmowę.")
        break
    response = model.invoke(user_input)
    print(response.content)