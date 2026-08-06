from flask import Flask, request, jsonify

app = Flask("server")

users = {}
messages = []


@app.route("/")
def home():
    return "Messenger server працює"


@app.route("/register", methods=["POST"])
def register():

    data = request.json

    phone = data["phone"]

    users[phone] = {
        "phone": phone
    }

    return jsonify({
        "status": "registered",
        "phone": phone
    })


@app.route("/send", methods=["POST"])
def send():

    data = request.json

    messages.append(data)

    return jsonify({
        "status": "sent"
    })


@app.route("/messages/<phone>")
def get_messages(phone):

    result = []

    for msg in messages:
        if msg["to"] == phone:
            result.append(msg)

    return jsonify(result)


app.run(host="0.0.0.0", port=5000)
