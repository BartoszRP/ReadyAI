
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Wczytanie klucza API z pliku .env
load_dotenv()
client = OpenAI()

app = Flask(__name__)

@app.route("/chat/hello")
def home():
    return render_template("index.html")

def send_message(message, previous_response_id):

    response = client.responses.create(
        model ="gpt-4.1-mini",
        input = message,
        previous_response_id = previous_response_id
    )
    return response.output_text, response.id


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data["message"]
    previous_response_id = data.get("previous_response_id")

    response, response_id=send_message(message, previous_response_id)

    return jsonify({
        "response": response,
        "response_id": response_id
    })

if __name__ == "__main__":
    app.run(debug=True)
