from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id]= InMemoryChatMessageHistory()
        store[session_id].add_message(SystemMessage("Jestes asystenem do rozwiazywania problemow"))
    return store[session_id]

model = init_chat_model(model="gpt-4.1-mini", model_provider="openai")

model_with_history = RunnableWithMessageHistory(model, get_session_history)

config = {"configurable":{"session_id":"ready4AI-chatbot"}}

while True:
    user_input = input("Ty: ")
    if user_input.lower() in {"quit", "exit", "stop", "koniec"}:
        print("Zakończono rozmowę.")
        break
    response = model_with_history.invoke(user_input,config)
    print("Asystent: " + response.content)
