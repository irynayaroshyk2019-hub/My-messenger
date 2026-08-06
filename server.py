from flask import Flask, request, jsonify

app = Flask(name)

users = {}
messages = []


@app.route("/")
def home():
    return "Messenger server працює"


@app.route("/register", methods=["POST"])
def register():

    data = request.json

    phone = data.get("phone")
    name = data.get("name", "Користувач")

    if not phone:
        return jsonify({
            "error": "No phone"
        }), 400

    users[phone] = {
        "name": name,
        "phone": phone
    }

    return jsonify({
        "status": "ok",
        "user": users[phone]
    })


@app.route("/contacts")
def contacts():

    return jsonify(
        list(users.values())
    )


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

    for message in messages:
        if (
            message.get("to") == phone
            or message.get("from") == phone
        ):
            result.append(message)

    return jsonify(result)


if name == "main":
    app.run(
        host="0.0.0.0",
        port=5000
    )
