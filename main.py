from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Chatbot API is running"}

@app.post("/chat")
def chat(msg: Message):
    text = msg.message.lower()
    if "hello" in text:
        return {"response": "Hi! How can I help you?"}
    elif "ai" in text:
        return {"response": "AI stands for Artificial Intelligence."}
    else:
        return {"response": "Sorry, I don't understand."}
