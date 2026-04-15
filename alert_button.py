import time
import RPi.GPIO as GPIO
import requests

BOT_TOKEN = "8604136663:AAEdQMfY2gIjvNVk-401zaAdq3Ldh7onRI0"
CHAT_ID = "6531197806"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

def send_telegram_message():
    url = f"https://api.telegram.org/bot8604136663:AAEdQMfY2gIjvNVk-401zaAdq3Ldh7onRI0/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "Someone pressed the alert button!"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        print("Telegram status:", response.status_code)
        print("Telegram response:", response.text)
    except Exception as e:
        print("Telegram error:", e)

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_telegram_message()
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)
