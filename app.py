from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "bachka_token"   
@app.route("/webhook", methods=["GET"])
def verify():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Message received:", data)  # Консол дээр ирсэн мессежийг харуулна
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
