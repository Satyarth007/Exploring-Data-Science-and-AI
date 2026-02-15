# RAG Chatbot --- Production Style AI Assistant

## Overview

This project is a production-style Retrieval Augmented Generation (RAG)
chatbot that combines:

-   Semantic search
-   Conversation memory
-   Personality prompting
-   Web interface
-   FastAPI backend

------------------------------------------------------------------------

## Architecture

Browser UI → FastAPI Server → Retriever → Knowledge Base → Memory →
Response Generator

------------------------------------------------------------------------

## Features

-   Semantic understanding using embeddings
-   Context-aware memory
-   Custom assistant personality
-   Lightweight web UI
-   Modular architecture for scaling

------------------------------------------------------------------------

## Project Structure

    rag-chatbot/
    │
    ├── app.py
    ├── retriever.py
    ├── memory.py
    ├── personality.py
    ├── knowledge.txt
    ├── requirements.txt
    └── templates/
        └── chat.html

------------------------------------------------------------------------

## Installation

Install dependencies:

    pip install fastapi uvicorn sentence-transformers numpy jinja2

------------------------------------------------------------------------

## Running the App

    uvicorn app:app --reload

Open browser:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## Modules Explained

### Retriever

Encodes documents into embeddings and retrieves the most semantically
similar text.

### Memory

Stores last few chat interactions to maintain conversation context.

### Personality

Defines assistant tone and response style.

### App Server

Handles API routes and response generation.

------------------------------------------------------------------------

## Knowledge Base

Stored inside `knowledge.txt`.\
You can expand it with domain-specific information.

------------------------------------------------------------------------

## How It Works

1.  User sends query
2.  Query converted into embedding
3.  Similar document retrieved
4.  Memory context added
5.  Response generated

------------------------------------------------------------------------

## Upgrade Ideas

-   Add FAISS vector database
-   Add Redis memory
-   Add real LLM integration
-   Add authentication
-   Deploy to cloud

------------------------------------------------------------------------

## Resume Description

Built a production-style Retrieval-Augmented chatbot with semantic
search, contextual memory, personality prompting, and web UI using
FastAPI and transformer embeddings.

------------------------------------------------------------------------

## License

Free to use for learning and experimentation.
