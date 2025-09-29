from flask import Flask, request
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # .env файл унших

app = Flask(__name__)

# ---------------- Config ----------------
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
FB_URL = "https://graph.facebook.com/v23.0/me/messages"




# ---------------- Helper ----------------
def send_message(recipient_id, message):
    print(">>> Sending message to", recipient_id)
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": recipient_id}, "message": message}
    r = requests.post(FB_URL, params=params, headers=headers, json=data)
    print(">>> Facebook API response:", r.status_code, r.text)


# ---------------- Эхлэх мэндчилгээ ----------------
def send_welcome_message(recipient_id):
    message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Сайн байна уу 👋 NANSA Crystal Europe-д тавтай морил!",
                        "image_url": "https://i.ibb.co/FLP67hGJ/Gemini-Generated-Image-u1h5hiu144555h5hiu1h5-copy-gigapixel-high-fidelity-v2-2x.png",
                        "subtitle": "Та доорх цэснээс сонгоно уу👇",
                        "buttons": [
                            {"type": "postback", "title": "💰 Үнийн мэдээлэл", "payload": "PRICE_INFO"},
                            {"type": "postback", "title": "📦 Хүргэлт ба захиалга", "payload": "ORDER_INFO"},
                            {"type": "postback", "title": "🕒 Цагийн хуваарь", "payload": "SCHEDULE_INFO"}
                        ]
                    },
                    {
                        "title": "🎁 Бэлгэнд тохиромжтой",
                        "image_url": "https://i.ibb.co/W4fX8j9q/Chat-GPT-Image-Jul-16-2025-12-47-57-PM-Recovered.png",
                        "subtitle": "Тансаг болор эдлэлүүдээс бэлэг сонгоорой 🎁",
                        "buttons": [
                            {"type": "postback", "title": "🎁 Бэлгийн бүтээгдэхүүн 1", "payload": "GIFT_PRODUCTS_1"},
                            {"type": "postback", "title": "🎁 Бэлгийн бүтээгдэхүүн 2", "payload": "GIFT_PRODUCTS_2"},
                            {"type": "postback", "title": "🎁 Бэлгийн бүтээгдэхүүн 3", "payload": "GIFT_PRODUCTS_3"}
                        ]
                    }
                ]
            }
        }
    }
    send_message(recipient_id, message)


# ---------------- Цагийн хуваарь ----------------
def send_schedule(recipient_id):
    schedule_text = (
        "🕒 Цагийн хуваарь:\n"
        "Даваа, Пүрэв: 14:00–16:00\n"
        "Мягмар–Ням: Зөвхөн утсаар холбогдоно.\n"
        "☎ 777 593 594"
    )
    send_message(recipient_id, {"text": schedule_text})
    message = {
        "attachment": {
            "type": "image",
            "payload": {"url": "https://i.ibb.co/Psv0xQHx/tsagiin-huviar-copy.jpg"}
        }
    }
    send_message(recipient_id, message)


# ---------------- Хаяг, утас ----------------
def send_contact(recipient_id):
    text = "📍 Хаяг: Česká 96, 434 01 Most\n☎ Утас: 777 593 594"
    send_message(recipient_id, {"text": text})


# ---------------- Хүргэлт ба захиалга ----------------
def send_order_info(recipient_id):
    text = (
        "📦 Хүргэлт ба захиалга:\n\n"
        "✈️ Монголоос захиалбал онгоцоор 7–14 хоногт хүргэгдэнэ.\n"
        "🚛 Газараар бол 1–2 сар болж байж хүргэгдэнэ.\n\n"
        "☎ Дэлгэрэнгүй мэдээлэл авах бол дараах дугаарт холбогдоно уу:\n"
        "777 593 594"
    )
    send_message(recipient_id, {"text": text})


# ---------------- Үнийн мэдээлэл ----------------
def send_products_batch1(recipient_id):
    elements = [
        {"title": "🥃 Виски сет", "image_url": "https://i.ibb.co/W4Jm3B7X/1.jpg", "subtitle": "Үнэ: 2500 крон",
         "buttons":[{"type":"postback","title":"⬇️ Дараагийн бүтээгдэхүүнүүд","payload":"MORE_PRODUCTS"}]},
        {"title": "🥂 Шампанскийн хундага", "image_url": "https://i.ibb.co/W4L412qR/2.jpg", "subtitle": "Үнэ: 1500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/zTNG1dTs/3.jpg", "subtitle": "Үнэ: 1600 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍭 Болор таваг", "image_url": "https://i.ibb.co/zTbGpGK1/4.jpg", "subtitle": "Үнэ: 1300-2500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Хундага – 6 ком", "image_url": "https://i.ibb.co/KksPKd6/5.jpg", "subtitle": "Үнэ: 2300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Дарсны хундага", "image_url": "https://i.ibb.co/FLNNJB6S/6.jpg", "subtitle": "Үнэ: 500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины Сэт", "image_url": "https://i.ibb.co/zHBjj02q/7.jpg", "subtitle": "Үнэ: 2800 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Графинтай хундаганы ком", "image_url": "https://i.ibb.co/qYT6JbTW/8.jpg", "subtitle": "Үнэ: 1800 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Хундага", "image_url": "https://i.ibb.co/kVh4Z0Gk/9.jpg", "subtitle": "Үнэ: 1500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine Crystal – 6 ширхэг", "image_url": "https://i.ibb.co/W4gjkx56/10.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)


def send_products_batch2(recipient_id):
    elements = [
        {"title": "🥂 2 Хос Хундага", "image_url": "https://i.ibb.co/84QKF4bL/11.jpg", "subtitle": "Үнэ: 500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍵 Цайны аяганы сет", "image_url": "https://i.ibb.co/DPmK7vS2/12.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины стакан", "image_url": "https://i.ibb.co/pr3ZzKcs/13.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Архины хундага", "image_url": "https://i.ibb.co/Rprf2BR6/14.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🎂 Тоортны суурь", "image_url": "https://i.ibb.co/jkJSLjR1/15.jpg", "subtitle": "Үнэ: 2000 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Болор таваг", "image_url": "https://i.ibb.co/QFTgMYhL/16.jpg", "subtitle": "Үнэ: 1500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine Crystal – 6 ширхэг", "image_url": "https://i.ibb.co/0pmDg567/17.jpg", "subtitle": "Үнэ: 1500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Хундага – 6 ком", "image_url": "https://i.ibb.co/4wHwFFGB/18.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Архины хундага", "image_url": "https://i.ibb.co/zTfQ2D0q/19.jpg", "subtitle": "Үнэ: 1200 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Болор аяга сет", "image_url": "https://i.ibb.co/qL4pbVp5/20.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)


# ---------------- Бэлгийн бүтээгдэхүүнүүд ----------------
def send_gift_products1(recipient_id):
    elements = [
        {"title": "🥃 Вискины Сэт", "image_url": "https://i.ibb.co/21nh5Btq/21.jpg", "subtitle": "Үнэ: 2100 крон",
         "buttons":[{"type":"postback","title":"⬇️ Дараагийн бэлэг","payload":"GIFT_PRODUCTS_2"}]},
        {"title": "🥃 Архины хундага", "image_url": "https://i.ibb.co/3mBCHvh1/22.jpg", "subtitle": "Үнэ: 1000 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Болор иж бүрдэл", "image_url": "https://i.ibb.co/G32QGwhc/23.jpg", "subtitle": "Үнэ: 4100 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/R4yn9dDY/24.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥤 Highball стакан", "image_url": "https://i.ibb.co/SXzjqzK6/25.jpg", "subtitle": "Үнэ: 2300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Графинтай ком", "image_url": "https://i.ibb.co/RGzw3sVD/26.jpg", "subtitle": "Үнэ: 3800 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/yBBbMBf8/27.jpg", "subtitle": "Үнэ: 2300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Дарсны хундага", "image_url": "https://i.ibb.co/4Dbj0sS/29.jpg", "subtitle": "Үнэ: 1500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🌸 Болор ваар", "image_url": "https://i.ibb.co/jvfd9grw/30.jpg", "subtitle": "Үнэ: 1000 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍭 Болор таваг", "image_url": "https://i.ibb.co/prdw2Gcp/32.jpg", "subtitle": "Үнэ: 1900 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)


def send_gift_products2(recipient_id):
    elements = [
        {"title": "🍵 Цайны аяганы сет", "image_url": "https://i.ibb.co/qLLsbYGv/33.jpg", "subtitle": "Үнэ: 1600 крон",
         "buttons":[{"type":"postback","title":"⬇️ Дараагийн бэлэг","payload":"GIFT_PRODUCTS_3"}]},
        {"title": "💎 Шампанск, Виски иж бүрдэл", "image_url": "https://i.ibb.co/G387xsr6/35.jpg", "subtitle": "Үнэ: 4500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍽️ Салфетка тогтоогч", "image_url": "https://i.ibb.co/6cJyVGmM/34.jpg", "subtitle": "Үнэ: 1200 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥤 Highball стакан", "image_url": "https://i.ibb.co/rfbfZgjT/37.jpg", "subtitle": "Үнэ: 2200 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины Сэт", "image_url": "https://i.ibb.co/Y4PPsXxY/36.jpg", "subtitle": "Үнэ: 2800 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine Crystal – 6 ширхэг", "image_url": "https://i.ibb.co/bwzggJf/38.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/bMKMMJ5K/39.jpg", "subtitle": "Үнэ: 4500 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥂 Шампанскийн хундага", "image_url": "https://i.ibb.co/vxM2JD4N/40.jpg", "subtitle": "Үнэ: 1400 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🌈 Өнгөт стакан", "image_url": "https://i.ibb.co/99jzHrnb/41.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Wine/Crystal", "image_url": "https://i.ibb.co/SXLvCCZm/42.jpg", "subtitle": "Үнэ: 1600 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)


def send_gift_products3(recipient_id):
    elements = [
        {"title": "🌸 Болор ваар", "image_url": "https://i.ibb.co/rRR0By0X/43.jpg", "subtitle": "Үнэ: 2100 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Коньякийн сет", "image_url": "https://i.ibb.co/1GLmBFkP/44.jpg", "subtitle": "Үнэ: 1800 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/mCszJhj5/45.jpg", "subtitle": "Үнэ: 1600 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🥃 Вискины Сэт", "image_url": "https://i.ibb.co/8gRdgF2S/46.jpg", "subtitle": "Үнэ: 2900 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍬 Чихрийн таваг", "image_url": "https://i.ibb.co/fVJNCY6K/47.jpg", "subtitle": "Үнэ: 1300 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "💎 Усны сет", "image_url": "https://i.ibb.co/j9ytjMSg/60.jpg", "subtitle": "Үнэ: 1400 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍷 Дарсны хундага", "image_url": "https://i.ibb.co/5Xwj4yqZ/57.jpg", "subtitle": "Үнэ: 1400 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍇 Жимсний таваг", "image_url": "https://i.ibb.co/tMC1hgFH/54.jpg", "subtitle": "Үнэ: 2600 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "🍽️ Салфетка тогтоогч", "image_url": "https://i.ibb.co/WCQFRj7/1200.jpg", "subtitle": "Үнэ: 1200 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]},
        {"title": "✨ Графин/Ус, Ундааны сав", "image_url": "https://i.ibb.co/6R5v4CwF/01200.jpg", "subtitle": "Үнэ: 1200 крон",
         "buttons":[{"type":"postback","title":"📞 Холбоо барих","payload":"CONTACT_INFO"}]}
    ]
    message = {"attachment":{"type":"template","payload":{"template_type":"generic","elements":elements}}}
    send_message(recipient_id, message)


# ---------------- Webhook ----------------
@app.route("/", methods=["GET"])
def home():
    return "Server is running!", 200


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verified!")
            return challenge, 200
        else:
            return "Invalid verification token", 403


    elif request.method == "POST":
        data = request.json
        print("Webhook received:", data)  # Debug log

        if "entry" in data:
            for entry in data["entry"]:
                if "messaging" in entry:
                    for msg in entry["messaging"]:
                        sender_id = msg["sender"]["id"]

                        if "message" in msg and "text" in msg["message"]:
                            text = msg["message"]["text"].lower()
                            if text in ["hi", "сайн уу", "сайн байна уу"]:
                                send_welcome_message(sender_id)

                        if "postback" in msg:
                            payload = msg["postback"]["payload"]
                            if payload == "PRICE_INFO":
                                send_products_batch1(sender_id)
                            elif payload == "MORE_PRODUCTS":
                                send_products_batch2(sender_id)
                            elif payload == "ORDER_INFO":
                                send_order_info(sender_id)
                            elif payload == "CONTACT_INFO":
                                send_contact(sender_id)
                            elif payload == "SCHEDULE_INFO":
                                send_schedule(sender_id)
                            elif payload == "GIFT_PRODUCTS_1":
                                send_gift_products1(sender_id)
                            elif payload == "GIFT_PRODUCTS_2":
                                send_gift_products2(sender_id)
                            elif payload == "GIFT_PRODUCTS_3":
                                send_gift_products3(sender_id)
                            elif payload == "GET_STARTED":
                                send_welcome_message(sender_id)

        return "EVENT_RECEIVED", 200


# ---------------- Run app ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)