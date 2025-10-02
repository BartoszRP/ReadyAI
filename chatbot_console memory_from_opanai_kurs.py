from dotenv import load_dotenv
from openai import OpenAI

# Wczytanie klucza API z pliku .env
load_dotenv()
client = OpenAI()

def choose_model() -> str:
    """Pozwala użytkownikowi wybrać model lub zakończyć program."""
    print("Dostępne modele: gpt-4.1-mini, gpt-5")
    while True:
        model = input("Wybierz model (lub wpisz 'quit' aby zakończyć): ").strip()
        if model.lower() == "quit":
            print("Zakończono program.")
            exit()
        if model in ["gpt-4.1-mini", "gpt-5"]:
            return model
        print("Niepoprawny model. Spróbuj ponownie.")

def send_message(message: str, model: str, previous_response_id: str = None) -> str:
    """Wysyła wiadomość do wybranego modelu i zwraca ID odpowiedzi."""
    if message.strip().lower() == "quit":
        print("Koniec rozmowy.")
        exit()

    response = client.responses.create(
        model=model,
        input=message,
        previous_response_id=previous_response_id
    )

    print(f"Bot: {response.output_text}")
    return response.id

def chat(model: str):
    """Rozpoczyna rozmowę z wybranym modelem."""
    print(f"Rozpoczynam rozmowę z modelem {model}. Aby zakończyć, wpisz 'quit'.")
    response_id = None
    while True:
        user_input = input("Ty [quit]: ")
        response_id = send_message(user_input, model, response_id)

def main():
    """Główna pętla programu z możliwością wielokrotnego wyboru modelu."""
    while True:
        model = choose_model()
        chat(model)

if __name__ == "__main__":
    main()
