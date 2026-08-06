from flask import Flask, request, jsonify

app = Flask(name)

users = []


@app.route("/")
def home():
    return "Messenger server працює"


@app.route("/register", methods=["POST"])
def register():

    data = request.json

    users.append(data)

    return jsonify({
        "status": "registered"
    })


@app.route("/users")
def get_users():

    return jsonify(users)


app.run(
    host="0.0.0.0",
    port=5000
)
