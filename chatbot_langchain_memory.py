from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

model = init_chat_model(model="gpt-4.1-mini", model_provider="openai")

message = [
    SystemMessage("Jestes asystenem inzyniera")
]

while True:
    user_input = input("Ty: ")
    message.append(HumanMessage(user_input))
    if user_input.lower() in {"quit", "exit", "stop", "koniec"}:
        print("Zakończono rozmowę.")
        break
    response = model.invoke(message)
    message.append(AIMessage(response.content))
    print(response.content)