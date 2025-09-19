from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "bachka_token"

@app.route("/", methods=["GET"])
def home():
    return "Server is running!", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Invalid verification token", 403

    if request.method == "POST":
        data = request.json
        print("Message received:", data)
        return "EVENT_RECEIVED", 200