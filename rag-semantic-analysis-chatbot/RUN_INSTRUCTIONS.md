
# Run Instructions — RAG Chatbot

## 1. Open Project Folder
Open terminal inside project directory.

## 2. Activate Virtual Environment
Windows:
```
.venv\Scripts\activate
```

Mac/Linux:
```
source .venv/bin/activate
```

---

## 3. Install Dependencies
```
pip install fastapi uvicorn sentence-transformers numpy jinja2
```

---

## 4. Start Server
```
py -m uvicorn app:app --reload
```

---

## 5. Open Browser
```
http://127.0.0.1:8000
```

---

## 6. Clear Chat Memory API
Endpoint:
```
GET /clear
```

Example:
```
http://127.0.0.1:8000/clear
```

Response:
```
{"status":"memory cleared"}
```

---

## Troubleshooting

### uvicorn not recognized
Run:
```
py -m uvicorn app:app --reload
```

### Missing libraries
```
pip install -r requirements.txt
```

---

## Dev Notes
- Memory stores last 3 messages
- Knowledge loaded at startup
- Embeddings cached

---

## Production Suggestions
- Replace memory with Redis
- Replace text file with vector DB
- Add authentication
- Add logging
