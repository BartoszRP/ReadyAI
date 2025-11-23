
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Wczytanie klucza API z pliku .env
load_dotenv()
client = OpenAI()

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/chat/hello")
def home():
    name = request.args.get("name", "nieznajomy człowieku")
    return render_template("index.html", title="Witaj w Flasku!", name=name)

def send_message(message, previous_response_id):

    response = client.responses.create(
        model ="gpt-4.1-mini",
        input = message,
        previous_response_id = previous_response_id
    )
    return response.output_text, response.id


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Ten endpoint przyjmuje POST z JSON-em. Idź na / albo /chat/hello."

    data = request.get_json(silent=True)
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data["message"]
    previous_response_id = data.get("previous_response_id")

    response_text, response_id = send_message(message, previous_response_id)

    return jsonify({"response": response_text, "response_id": response_id})

if __name__ == "__main__":
    app.run(debug=True)
