
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from retriever import retrieve
from memory import store, get_context, chat_memory
from personality import PERSONALITY

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def generate_response(query):
    context = get_context()
    fact = retrieve(query)

    reply = f"""
{PERSONALITY}

Conversation so far:
{context}

Relevant knowledge:
{fact}

Answer:
{fact}
"""
    return reply.strip()


@app.get("/", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.get("/chat")
def chat(q: str):
    answer = generate_response(q)
    store(q, answer)
    return {"response": answer}


@app.get("/clear")
def clear_memory():
    chat_memory.clear()
    return JSONResponse({"status": "memory cleared"})
