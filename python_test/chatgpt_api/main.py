import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Set your API key and proxy information
API_KEY = "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"
PROXY_HOST = "127.0.0.1"
PROXY_PORT = "7890"
SHOW_NUMS = 10


class Message(BaseModel):
    text: str


conn = sqlite3.connect("messages.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, text TEXT)")
conn.commit()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, page: int = 1):
    offset = (page - 1) * SHOW_NUMS
    rows = cursor.execute("SELECT * FROM messages ORDER BY id DESC LIMIT ? OFFSET ?", (SHOW_NUMS, offset)).fetchall()
    messages = [{"question": row[1], "text": row[2]} for row in rows]
    print(page, offset, len(messages))
    return templates.TemplateResponse("home.html", {"request": request, "messages": messages, "page": page, "num_messages_to_display": SHOW_NUMS})


@ app.post("/")
async def ask_question(request: Request, question: str = Form(...)):
    message = await get_response(question)
    cursor.execute("INSERT INTO messages (question, text) VALUES (?, ?)", (question, message,))
    conn.commit()
    return {"answer": message}


async def get_response(question: str):
    proxies = {
        "http": f"http://{PROXY_HOST}:{PROXY_PORT}",
        "https": f"http://{PROXY_HOST}:{PROXY_PORT}"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{question}"}],
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, proxies=proxies)
    return response.json().get('choices')[0]['message']['content'].strip()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
