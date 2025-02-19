from instagrapi import Client
import time
import random
import sys
import os
from datetime import datetime

# Login credentials
USERNAME = "bot.t5le3"
PASSWORD = "Abdulaziz7!"
RECIPIENT_USERNAME = "yilxlu"
SESSION_FILE = "session.json"

messages = [
    "والله لا اهكرك",
    "هلامنى",
    "هاي انا بوت",
    "وينك",
    "قومي دوام",
    "هههههههههههههههههههههههههههههههههه",
    "قم الساعه 8 الحين قدامي عالحامعه بسرعه",
    "تراني اقول كلام وصخ انتبهي",
    "زق",
    "يا حيوانه",
    "داله",
    "بلعنمك",
    "https://bit.ly/40qpkVa",
    "ياورع",
    "من يبغاني اتوطى ببطنه ",
    "استغفرالله",
    "اللهم صلي وسلم على نبينامحمد",
    "انا بوت",
    "اذا ماحركت الرساله ذي نصروياتك, فاحسن الله عزاك في نفسك, شف اقسم بالله اغلى ما املك مستعد ابيعه مقابل الفوز اليوم",
    "https://youtu.be/wYyRimdbWno?si=XL9vazYKqCgjhp9j",
    "يا دكتوره",
    "https://youtu.be/EuAfKjDVVUM?si=Dw3iDN89cH2TmSVb",
]

# Create client object
cl = Client()

# Check if session file exists
if os.path.exists(SESSION_FILE):
    print("🔹 Loading saved session...")
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)
else:
    print("🔹 Logging in and saving session...")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)

def send_random_message():
    """ Send a random message immediately """
    message = random.choice(messages)
    user_id = cl.user_id_from_username(RECIPIENT_USERNAME)
    cl.direct_send(message, user_ids=[user_id])
    print(f"[{datetime.now()}] ✅ Message sent successfully to {RECIPIENT_USERNAME}: {message}")

# Send a few messages immediately for testing
for _ in range(random.randint(3, 10)):  # Adjust the number of messages to send immediately
    send_random_message()
    sleep_time = random.randit(30 , 90 )
        print(f"Waiting {sleep_time} seconds before next message...")

    time.sleep(sleep_time)  # Short delay between messages to avoid spam detection

print("✅ Bot execution completed successfully.")
sys.exit(0)
