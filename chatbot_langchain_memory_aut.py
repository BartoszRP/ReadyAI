from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

model = init_chat_model(model="gpt-4.1-mini", model_provider="openai")

chat_history = InMemoryChatMessageHistory()

chat_history.add_message(SystemMessage("Jestes asystenemt do rozwiazania problemow"))

while True:
    user_input = input("Ty: ")
    chat_history.add_user_message(user_input)
    if user_input.lower() in {"quit", "exit", "stop", "koniec"}:
        print("Zakończono rozmowę.")
        break
    response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(response.content)
    print("Asystent: " + response.content)