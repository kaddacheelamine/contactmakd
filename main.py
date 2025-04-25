from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests
import os


def sender(msg):
# استبدل القيم التالية بما يناسبك
    bot_token = os.getenv('BT_TOKEN') # توكن البوت من BotFather
    user_id = os.getenv('BU_TOKEN')  # معرف المستخدم الذي تريد إرسال الرسالة له
    message = msg

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': user_id,
        'text': message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('send  sec')
    else:
        print(f'not {response.text}')


app = FastAPI()

# Optional: Allow requests from your frontend (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/contact")
async def receive_contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    sender(f"{name} \n {email} \n {subject} \n {message}  ")
    return {"status": "received"}
