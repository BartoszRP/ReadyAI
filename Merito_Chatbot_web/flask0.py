from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("flask0.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
