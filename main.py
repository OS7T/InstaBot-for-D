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
for _ in range(random.randint(3, 5)):  # Adjust the number of messages to send immediately
    send_random_message()
    time.sleep(5)  # Short delay between messages to avoid spam detection

print("✅ Bot execution completed successfully.")
sys.exit(0)
