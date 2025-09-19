from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "bachka_token"
PAGE_ACCESS_TOKEN = "EAAZAmrUlytb0BPYg7ucghGA1pNTdrluj3QLKm924bF8yk7DMC02H9rWDRWD55Vl2aQNFNSec5iF7Y7XyPRXYnx58r1PU5gNJgCbejNy2XhWZBJYRa5eIZCFZA8TD4SytUum2bfAidLdgMmCdWZAJk2rGZBm11HZAMi20QqZAv4ksvDRE52Duhpe8tHsRK2MXVtK55uZBVJpqF"

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

        # Messenger-ээс ирсэн мессежийг шалгаж хариу өгөх
        if "entry" in data:
            for entry in data["entry"]:
                if "messaging" in entry:
                    for msg in entry["messaging"]:
                        if "message" in msg:
                            sender_id = msg["sender"]["id"]
                            text = msg["message"].get("text")

                            # Энгийн автомат хариу илгээх
                            if text:
                                send_message(sender_id, f"Чиний бичсэн: {text}")

        return "EVENT_RECEIVED", 200

def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v23.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    requests.post(url, params=params, headers=headers, json=data)
