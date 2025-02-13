from instagrapi import Client

# بيانات تسجيل الدخول
USERNAME = "bot.t5le3"
PASSWORD = "Abdulaziz7!"

# إنشاء عميل Instagram
cl = Client()

# تسجيل الدخول
cl.login(USERNAME, PASSWORD)

# حفظ الجلسة في ملف
cl.dump_settings("session.json")

print("✅ تم حفظ الجلسة بنجاح في 'session.json'.")
