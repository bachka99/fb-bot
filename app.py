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
                        "image_url": "https://i.ibb.co/FLP67hGJ/Gemini-Generated-Image-u1h5hiu144555h5hiu1h5-copy-gigapixel-high-fidelity-v2-2x.png",  # Cover зураг
                        "subtitle": "Та доорх цэснээс сонгоно уу👇",
                        "buttons": [
                            {"type": "postback", "title": "💰 Үнийн мэдээлэл", "payload": "PRICE_INFO"},
                            {"type": "postback", "title": "🕒 Цагийн хуваарь", "payload": "SCHEDULE_INFO"},
                            {"type": "postback", "title": "📍 Хаяг, утас", "payload": "CONTACT_INFO"}
                        ]
                    },
                    {
                        "title": "🎁 Бэлгэнд тохиромжтой",
                        "image_url": "https://i.ibb.co/8B2bR9X/tsagiin-huviar.png",  # Энд бэлгийн зураг тавьбал илүү гоё харагдана
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
