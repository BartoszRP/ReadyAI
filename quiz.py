from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()
store = {}

quiz_subject = input("Podaj temat quizu (np. Stolice Europy, Państwa Azji, Literatura Polski): ").strip()
if not quiz_subject:
    print("Nie podano tematu. Kończę.")
    exit()

try:
    num_questions = int(input("Podaj liczbę pytań w quizie (np. 2 do 20): ").strip())
    if num_questions < 1 or num_questions > 20:
        raise ValueError
except ValueError:
    print("Nieprawidłowa liczba pytań. Kończę.")
    exit()


def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
        store[session_id].add_message(SystemMessage(
            f"""
            Jesteś mistrzem quizu o {quiz_subject}.
            Przeprowadź quiz złożony z dokładnie {num_questions} pytań, po jednym na raz.
            Każde pytanie ma mieć 4 możliwe odpowiedzi oznaczone literami a), b), c), d), 
            z których tylko jedna jest poprawna.
            Po każdym pytaniu czekaj na odpowiedź użytkownika.
            Za poprawną odpowiedź napisz: 'Dobrze!'.
            Za błędną odpowiedź napisz: 'Błąd! Poprawna odpowiedź to X) ...', 
            gdzie X to litera poprawnej odpowiedzi oraz pełna treść tej odpowiedzi.
            Po {num_questions} pytaniu podaj wynik w stylu: 'Twój wynik to Y na {num_questions}.'
            Następnie:
            - Jeśli użytkownik uzyskał co najmniej 60% poprawnych odpowiedzi, napisz: 'Zdałeś!'
            - Jeśli poniżej 60% poprawnych odpowiedzi, napisz: 'Nie zdałeś.'
            Po tej informacji zakończ quiz, pisząc wyłącznie słowo 'koniec'.
            Każde pytanie powinno dotyczyć innego zagadnienia lub kraju – 
            **nie powtarzaj pytań** w trakcie jednego quizu.
            Nie pisz żadnych komentarzy, żartów, powitań ani podsumowań poza powyższymi instrukcjami.
            Prowadź całą rozmowę w języku polskim.

            Przykład przebiegu rozmowy:

            Pytanie 1: Jaka jest stolica Polski?
            a) Warszawa
            b) Berlin
            c) Praga
            d) Wiedeń

            Użytkownik: a
            Dobrze!

            ...

            Twój wynik to 8 na 13.
            Zdałeś!
            koniec
            
            Twój wynik to 5 na 13.
            Nie zdałeś.
            koniec

            """
        ))

    return store[session_id]


model = init_chat_model(model="gpt-4.1-mini", model_provider="openai")
model_with_history = RunnableWithMessageHistory(model, get_session_history)
config = {"configurable": {"session_id": "ready4AI-quiz"}}

print("**********************************************************************************************************")
print(f"Quiz o {quiz_subject}! Liczba pytań: {num_questions} - odpowiadaj literami a/b/c/d. Wyjdź przez 'koniec'.")
print("**********************************************************************************************************")

print("Czy jesteś gotowy? Napisz 'start', żeby zacząć, albo 'koniec', żeby wyjść.")

while True:
    user_input = input("Ty: ").strip().lower()
    if user_input == "start":
        break
    elif user_input in {"koniec", "quit", "exit", "stop"}:
        print("Koniec quizu.")
        exit()
    else:
        print("Napisz 'start', żeby zacząć, albo 'koniec', żeby wyjść.")

user_input = "Zaczynaj quiz"

while True:
    response = model_with_history.invoke(user_input, config)
    print("Asystent:", response.content)
    if "twój wynik" in response.content.lower():
        break
    user_input = input("Ty: ").strip()
    if user_input.lower() in {"koniec", "quit", "exit", "stop"}:
        print("Koniec quizu.")
        break
