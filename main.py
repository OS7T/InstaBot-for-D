from instagrapi import Client
import time
import random
import schedule
from datetime import datetime
import sys
import os

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
    """ Send a random message between 8:00 - 9:00 AM """
    message = random.choice(messages)
    user_id = cl.user_id_from_username(RECIPIENT_USERNAME)
    cl.direct_send(message, user_ids=[user_id])
    print(f"[{datetime.now()}] ✅ Message sent successfully to {RECIPIENT_USERNAME}: {message}")

def schedule_random_messages():
    """ Schedule messages at random times between 8:00 - 9:00 AM """
    for _ in range(random.randint(3, 7)):  # Number of random messages per day (between 3 to 7)
        random_minute = random.randint(0, 59)
        scheduled_time = f"08:{random_minute:02d}"  # Format HH:MM
        schedule.every().day.at(scheduled_time).do(send_random_message)
        print(f"📅 Message scheduled at {scheduled_time}")

# Schedule messages
schedule_random_messages()

# Run scheduled tasks with a set timeout
start_time = time.time()
timeout = 180  # Run bot for 3 minutes then exit

while time.time() - start_time < timeout:
    schedule.run_pending()
    time.sleep(10)  # Wait between each check to avoid excessive resource usage

print("✅ Bot execution completed successfully.")
sys.exit(0)  # Exit program after tasks are done
