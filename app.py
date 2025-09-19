from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "bachka_token"
PAGE_ACCESS_TOKEN = "EAAZAmrUlytb0BPYg7ucghGA1pNTdrluj3QLKm924bF8yk7DMC02H9rWDRWD55Vl2aQNFNSec5iF7Y7XyPRXYnx58r1PU5gNJgCbejNy2XhWZBJYRa5eIZCFZA8TD4SytUum2bfAidLdgMmCdWZAJk2rGZBm11HZAMi20QqZAv4ksvDRE52Duhpe8tHsRK2MXVtK55uZBVJpqF"

# --- Үндсэн цэс ---
def send_welcome_message(recipient_id):
    url = "https://graph.facebook.com/v23.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": "Сайн байна уу 👋 Та сонирхож буй үйлчилгээгээ сонгоно уу:",
            "quick_replies": [
                {"content_type": "text", "title": "💰 Үнийн мэдээлэл", "payload": "PRICE_INFO"},
                {"content_type": "text", "title": "🎁 Бэлгэнд тохиромжтой", "payload": "GIFT"},
                {"content_type": "text", "title": "🕒 Цагийн хуваарь", "payload": "SCHEDULE"},
                {"content_type": "text", "title": "📍 Хаяг, утас", "payload": "CONTACT"}
            ]
        }
    }
    requests.post(url, params=params, headers=headers, json=data)

# --- Үнийн мэдээлэл ---
def send_price_info(recipient_id):
    url = "https://graph.facebook.com/v23.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": (
                "Манай дэлгүүр дээр 60 гаруй нэр төрлийн болор эдлэлүүд худалдаалагдаж байна ✅\n\n"
                "Үнийн дүн нь хэлбэр хэмжээнээсээ хамаараад 500 - 9000 крон-ийн хооронд худалдаалагдаж байна 💰\n\n"
                "Доорх загваруудаас сонгоод дэлгэрэнгүй үзээрэй 👇"
            )
        }
    }
    requests.post(url, params=params, headers=headers, json=data)

    # --- Жишээ загварууд (carousel) ---
    carousel = {
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Виски сет",
                            "image_url": "https://www.facebook.com/photo.php?fbid=122111849876133928&set=pb.61554017856554.-2207520000&type=3",
                            "subtitle": "Үнэ: 2500 крон",
                            "buttons": [
                                {"type": "postback", "title": "📍 Хаяг, утас", "payload": "CONTACT"}
                            ]
                        },
                        {
                            "title": "Шампанскийн хундага",
                            "image_url": "https://www.facebook.com/photo.php?fbid=122111997602133928&set=pb.61554017856554.-2207520000&type=3",
                            "subtitle": "Үнэ: 1500 крон",
                            "buttons": [
                                {"type": "postback", "title": "📍 Хаяг, утас", "payload": "CONTACT"}
                            ]
                        },
                        {
                            "title": "Чихрийн таваг",
                            "image_url": "https://www.facebook.com/photo.php?fbid=122112045140133928&set=pb.61554017856554.-2207520000&type=3",
                            "subtitle": "Үнэ: 1600 крон",
                            "buttons": [
                                {"type": "postback", "title": "📍 Хаяг, утас", "payload": "CONTACT"}
                            ]
                        }
                    ]
                }
            }
        }
    }
    requests.post(url, params=params, headers=headers, json=carousel)

# --- Бэлгэнд тохиромжтой ---
def send_gift_info(recipient_id):
    send_message(recipient_id, "🎁 Манай болор эдлэлүүд бэлэгт хамгийн тохиромжтой ✨")

# --- Цагийн хуваарь ---
def send_schedule(recipient_id):
    url = "https://graph.facebook.com/v23.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": "https://www.facebook.com/photo/?fbid=122236977290133928&set=a.122101765010133928",                    "is_reusable": True
                }
            }
        }
    }
    requests.post(url, params=params, headers=headers, json=data)

# --- Хаяг, утас ---
def send_contact_info(recipient_id):
    send_message(
        recipient_id,
        "📍 Хаяг: Česká 96, 434 01 Most\n📞 Утас: 777 593 594\n\nТа бидэнтэй холбогдоорой 😊"
    )

# --- Ердийн мессеж илгээх функц ---
def send_message(recipient_id, message_text):
    url = "https://graph.facebook.com/v23.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    requests.post(url, params=params, headers=headers, json=data)

# --- Flask webhook ---
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
        if "entry" in data:
            for entry in data["entry"]:
                if "messaging" in entry:
                    for msg in entry["messaging"]:
                        sender_id = msg["sender"]["id"]

                        if "message" in msg and "text" in msg["message"]:
                            text = msg["message"]["text"].lower()

                            if text in ["hi", "hello", "сайн уу", "сайн байна уу"]:
                                send_welcome_message(sender_id)

                            elif "үнэ" in text:
                                send_price_info(sender_id)

                            elif "бэлэг" in text:
                                send_gift_info(sender_id)

                            elif "цаг" in text:
                                send_schedule(sender_id)

                            elif "хаяг" in text or "утас" in text:
                                send_contact_info(sender_id)

                            else:
                                send_message(sender_id, "🤖 Сонгосон үйлчилгээгээ үндсэн цэснээс дарна уу.")
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
