from fastapi import FastAPI
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

from fastapi import  Request
from pydantic import BaseModel



class ContactForm(BaseModel):
    name: str
    email: str
    subject: str
    message: str

@app.post("/contact")
async def receive_contact(data: ContactForm):
    print(f"Name: {data.name}")
    print(f"Email: {data.email}")
    print(f"Subject: {data.subject}")
    print(f"Message: {data.message}")
    sender(f"Name: {data.name} \n Email: {data.email} \n Subject: {data.subject} \n Message: {data.message} ")
    return {"status": "received"}

