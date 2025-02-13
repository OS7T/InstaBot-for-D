from instagrapi import Client
import time
import random
import schedule
from datetime import datetime


USERNAME = "bot.t5le3"
PASSWORD = "Abdulaziz7!"
RECIPIENT_USERNAME = "yilxlu"

messages = [
    "والله لا اهكرك",
    "هلامنى",
   "هاي انا بوت"
   "وينك"
   "قومي دوام"
   "هههههههههههههههههههههههههههههههههه"
     "قم الساعه 8 الحين قدامي عالحامعه بسرعه",
]

cl = Client()
cl.login(USERNAME, PASSWORD)

def send_random_message():
    """ إرسال رسالة عشوائية في وقت عشوائي بين 8:00 - 9:00 صباحًا """
    message = random.choice(messages)
    user_id = cl.user_id_from_username(RECIPIENT_USERNAME)
    cl.direct_send(message, user_ids=[user_id])
    print(f"[{datetime.now()}] send seccusfle {RECIPIENT_USERNAME}: {message}")

def schedule_random_messages():
    """ جدولة الرسائل في أوقات عشوائية بين 8:00 - 9:00 صباحًا """
    for _ in range(random.randint(3, 7)):  # عدد الرسائل العشوائي يوميًا (بين 3 إلى 7)
        random_minute = random.randint(0, 59)
        scheduled_time = f"08:{random_minute:02d}"  # صيغة HH:MM
        schedule.every().day.at(scheduled_time).do(send_random_message)
        print(f"📅 massge request on time {scheduled_time}")

# جدولة الرسائل كل يوم الساعة 8 صباحًا مع أوقات عشوائية
schedule.every().day.at("08:00").do(schedule_random_messages)

print("bot start work ")

# تشغيل الجدولة باستمرار
while True:
    schedule.run_pending()
    time.sleep(30)  # التحقق كل 30 ثانية

