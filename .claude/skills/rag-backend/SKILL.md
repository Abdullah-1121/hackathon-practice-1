---
name: rag-backend
description: Expert in building RAG backends using FastAPI, Qdrant Cloud, and Google Gemini Embeddings. Use this for creating the python server and indexing scripts.
allowed-tools: [Read, Write, Bash]
---

# Gemini-Powered RAG Backend Instructions

## 1. Technology Stack
- **Framework:** FastAPI (`pip install fastapi uvicorn`)
- **Vector DB:** Qdrant Cloud (`pip install qdrant-client`)
- **Embeddings:** Google Gemini (`pip install google-generativeai`)

## 2. Standard `main.py` Structure
When asked to build the server, create a `main.py` with this flow:
1.  **Setup:**
    - Configure `genai` with `os.getenv("GOOGLE_API_KEY")`.
    - Connect to Qdrant using the cloud URL.
2.  **The `/chat` Endpoint:**
    - Accept user query.
    - **Generate Embedding:** Use `genai.embed_content(model="models/text-embedding-004", content=query)` to get the vector.
    - **Search:** Pass that vector to `qdrant_client.search()`.
    - **Answer:** Send the found text + query to the LLM.

## 3. Indexing Rule (Critical Change)
You CANNOT use Qdrant's auto-embedding feature. You must script the loop manually in `scripts/index_book.py`:
1.  Read the markdown file.
2.  Split into chunks (approx 500 chars).
3.  **Loop through chunks:**
    - Call `genai.embed_content(model="models/text-embedding-004", content=chunk)`.
    - **Wait 1 second** (`time.sleep(1)`) between calls to avoid hitting Free Tier Rate Limits.
    - Store the result in a list.
4.  Upload the list of vectors to Qdrant using `client.upsert()`.
