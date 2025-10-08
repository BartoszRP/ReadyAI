from dotenv import load_dotenv
from openai import OpenAI

# Wczytanie klucza API z pliku .env
load_dotenv()
client = OpenAI()


def choose_model() -> str:
    """Pozwala użytkownikowi wybrać model lub zakończyć program."""
    print("Dostępne modele: gpt-4o-mini, gpt-4o, gpt-3.5-turbo")
    while True:
        model = input("Wybierz model (lub wpisz 'quit' aby zakończyć): ").strip()
        if model.lower() == "quit":
            print("Zakończono program.")
            exit()
        if model in ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]:
            return model
        print("Niepoprawny model. Spróbuj ponownie.")


def send_message(message: str, model: str, conversation_history: list) -> str:
    """Wysyła wiadomość do wybranego modelu i zwraca odpowiedź."""
    if message.strip().lower() == "quit":
        print("Koniec rozmowy.")
        exit()

    # Dodaj wiadomość użytkownika do historii
    conversation_history.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model=model, messages=conversation_history, max_tokens=1000, temperature=0.7
        )

        bot_response = response.choices[0].message.content
        print(f"Bot: {bot_response}")

        # Dodaj odpowiedź bota do historii
        conversation_history.append({"role": "assistant", "content": bot_response})

        return bot_response

    except Exception as e:
        print(f"Błąd podczas komunikacji z API: {e}")
        return ""


def chat(model: str):
    """Rozpoczyna rozmowę z wybranym modelem."""
    print(f"Rozpoczynam rozmowę z modelem {model}. Aby zakończyć, wpisz 'quit'.")
    conversation_history = []
    while True:
        user_input = input("Ty [quit]: ")
        send_message(user_input, model, conversation_history)


def main():
    """Główna pętla programu z możliwością wielokrotnego wyboru modelu."""
    while True:
        model = choose_model()
        chat(model)


if __name__ == "__main__":
    main()
