from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "bachka_token"
PAGE_ACCESS_TOKEN = "EAAZAmrUlytb0BPYg7ucghGA1pNTdrluj3QLKm924bF8yk7DMC02H9rWDRWD55Vl2aQNFNSec5iF7Y7XyPRXYnx58r1PU5gNJgCbejNy2XhWZBJYRa5eIZCFZA8TD4SytUum2bfAidLdgMmCdWZAJk2rGZBm11HZAMi20QqZAv4ksvDRE52Duhpe8tHsRK2MXVtK55uZBVJpqF"   # өөрийн Page Access Token-оо энд тавина

FB_URL = "https://graph.facebook.com/v23.0/me/messages"

def send_message(recipient_id, message):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": recipient_id}, "message": message}
    requests.post(FB_URL, params=params, headers=headers, json=data)

# ---------------- Эхлэх мэндчилгээ ----------------
def send_welcome_message(recipient_id):
    message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Сайн байна уу 👋 NANSA Crystal Europe-oos Болорын дэлгүүрт тавтай морил!",
                        "image_url": "https://i.ibb.co/FLP67hGJ/Gemini-Generated-Image-u1h5hiu144555h5hiu1h5-copy-gigapixel-high-fidelity-v2-2x.png",
                        "subtitle": "Та доорх цэснээс сонгоно уу👇",
                        "buttons": [
                            {"type": "postback", "title": "💰 Үнийн мэдээлэл", "payload": "PRICE_INFO"},
                            {"type": "postback", "title": "🕒 Цагийн хуваарь", "payload": "SCHEDULE_INFO"},
                            {"type": "postback", "title": "📍 Хаяг, утас", "payload": "CONTACT_INFO"}
                        ]
                    },
                    {
                        "title": "🎁 Бэлгэнд тохиромжтой",
                        "image_url": "https://i.ibb.co/W4fX8j9q/Chat-GPT-Image-Jul-16-2025-12-47-57-PM-Recovered.png",
                        "subtitle": "Тансаг болор эдлэлүүдээс бэлэг сонгоорой 🎁",
                        "buttons": [
                            {"type": "postback", "title": "Бэлгийн загварууд", "payload": "GIFT_PRODUCTS"}
                        ]
                    }
                ]
            }
        }
    }
    send_message(recipient_id, message)

# ---------------- Цагийн хуваарь ----------------
def send_schedule(recipient_id):
    message = {
        "attachment": {
            "type": "image",
            "payload": {
                "url": "https://i.ibb.co/HfP7qP1P/tsagiin-huviar-copy.jpg"
            }
        }
    }
    send_message(recipient_id, message)

# ---------------- Хаяг, утас ----------------
def send_contact(recipient_id):
    text = "📍 Хаяг: Česká 96, 434 01 Most\n☎ Утас: 777 593 594"
    send_message(recipient_id, {"text": text})

# ---------------- Бүтээгдэхүүн - Эхний 10 ----------------
def send_products_batch1(recipient_id):
    elements = [
        {"title": "🥃 Виски сет", "image_url": "https://www.facebook.com/photo.php?fbid=122111849876133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 2500 крон", "buttons":[{"type":"postback","title":"➡ Дараагийн загварууд","payload":"MORE_PRODUCTS"}]},
        {"title": "🥂 Шампанскийн хундага", "image_url": "https://www.facebook.com/photo.php?fbid=122111997602133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://www.facebook.com/photo.php?fbid=122112045140133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1600 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🍬🍭 Болор чихрийн таваг", "image_url": "https://www.facebook.com/photo.php?fbid=122237009726133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1300-2500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Шампанскийн хундага – 6 ком", "image_url": "https://www.facebook.com/photo.php?fbid=122237013440133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 2300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Дарсны хундага", "image_url": "https://www.facebook.com/photo.php?fbid=122112039968133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины Сэт", "image_url": "https://www.facebook.com/photo.php?fbid=122112030548133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 2800 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥃🍷 Графинтай болор хундаганы ком", "image_url": "https://www.facebook.com/photo.php?fbid=122111878076133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1800 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Шампанскийн хундага", "image_url": "https://www.facebook.com/photo.php?fbid=122112031310133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine Crystal – 6 ширхэгтэй сет", "image_url": "https://www.facebook.com/photo/?fbid=122111864738133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)

# ---------------- Бүтээгдэхүүн - Дараагийн 10 ----------------
def send_products_batch2(recipient_id):
    elements = [
        {"title": "🥂 2 Хос Шампанскийн хундага", "image_url": "https://www.facebook.com/photo/?fbid=122112005744133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🍵☕ Цайны аяганы сет", "image_url": "https://www.facebook.com/photo/?fbid=122112005606133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины болор стакан", "image_url": "https://www.facebook.com/photo/?fbid=122111984276133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Архины хундага", "image_url": "https://www.facebook.com/photo.php?fbid=122111850050133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🎂💎 Болор тоортны суурь", "image_url": "https://www.facebook.com/photo.php?fbid=122111850050133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 2000 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "💎 Болор таваг", "image_url": "https://www.facebook.com/photo/?fbid=122111851532133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine Crystal – 6 ширхэгтэй сет", "image_url": "https://www.facebook.com/photo/?fbid=122111856104133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1500 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Шампанскийн хундага – 6 ком", "image_url": "https://www.facebook.com/photo.php?fbid=122111866004133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Архины хундага", "image_url": "https://www.facebook.com/photo/?fbid=122111916506133928&set=pb.61554017856554.-2207520000", "subtitle": "Үнэ: 1200 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]},
        {"title": "💎 Болор аяга, хундаганы сет", "image_url": "https://www.facebook.com/photo.php?fbid=122112004436133928&set=pb.61554017856554.-2207520000&type=3", "subtitle": "Үнэ: 1300 крон", "buttons":[{"type":"postback","title":"📍 Хаяг","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)

# ---------------- Webhook ----------------
@app.route("/", methods=["GET"])
def home():
    return "Server is running!", 200

@app.route("/webhook", methods=["GET","POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Invalid verification token", 403

    elif request.method == "POST":
        data = request.json
        if "entry" in data:
            for entry in data["entry"]:
                if "messaging" in entry:
                    for msg in entry["messaging"]:
                        sender_id = msg["sender"]["id"]

                        if "message" in msg and "text" in msg["message"]:
                            text = msg["message"]["text"].lower()
                            if text in ["hi","сайн уу","сайн байна уу"]:
                                send_welcome_message(sender_id)

                        if "postback" in msg:
                            payload = msg["postback"]["payload"]
                            if payload == "PRICE_INFO":
                                send_products_batch1(sender_id)
                            elif payload == "MORE_PRODUCTS":
                                send_products_batch2(sender_id)
                            elif payload == "CONTACT_INFO":
                                send_contact(sender_id)
                            elif payload == "SCHEDULE_INFO":
                                send_schedule(sender_id)
                            elif payload == "GIFT_PRODUCTS":
                                send_products_batch1(sender_id)
        return "EVENT_RECEIVED", 200
