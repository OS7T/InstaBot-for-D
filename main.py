from instagrapi import Client
import time
import random
import schedule
from datetime import datetime

USERNAME = "bot.t5le3"
PASSWORD = "Abdulaziz7!"

cl = Client()

# تحميل الجلسة المحفوظة إذا كانت موجودة
try:
    cl.load_settings("session.json")
    cl.login(USERNAME, PASSWORD)
    print("✅ save sesstion succesfuly.")
except:
    print("⚠️ there is no session")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings("session.json")  # حفظ الجلسة لاستخدامها لاحقًا

print("✅ login to Instagram succes")

messages = [
    "والله لا اهكرك",
    "هلاااا",
    "هاي انا بوت",
    "وينك",
    "قومي دوام",
    "😂😂😂😂😂😂😂😂😂😂",
    "قم الساعه 8 الحين قدامي عالحامعه بسرعه",
]

def send_random_message():
    """ إرسال رسالة عشوائية في وقت عشوائي بين 8:00 - 9:00 صباحًا """
    message = random.choice(messages)
    user_id = cl.user_id_from_username("yilxlu")
    cl.direct_send(message, user_ids=[user_id])
    print(f"[{datetime.now()}] send succesful to yilxlu: {message}")

schedule.every().day.at("08:30").do(send_random_message)

print("✅ bot ready to work ")

while True:
    schedule.run_pending()
    time.sleep(30)
