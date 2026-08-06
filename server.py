from flask import Flask, request, jsonify

app = Flask("server")

messages = []

@app.route("/")
def home():
    return "Messenger server працює"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data)
    return jsonify({"status": "sent"})

@app.route("/messages")
def get_messages():
    return jsonify(messages)

app.run(host="0.0.0.0", port=5000)
