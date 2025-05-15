from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
import requests, os
from utils.gmail import send_email
from utils.telegram import send_telegram
from utils.whatsapp import send_whatsapp

app = FastAPI()

class RequestModel(BaseModel):
    user_input: str
    context: str

@app.post("/process/")
async def process(request: RequestModel):
    command = request.user_input.lower()
    if "telegram" in command:
        return {"response": send_telegram(command)}
    elif "gmail" in command:
        return {"response": send_email(command)}
    elif "whatsapp" in command:
        return {"response": send_whatsapp(command)}
    else:
        return {"response": "No matching service found in command."}
