import os

import google.generativeai as genai  # <--- FIX 1: Standard Import
from qdrant_client import QdrantClient, models

from src.services.gemini_client import get_gemini_model
from src.services.qdrant_client import qdrant_client

# <--- FIX 1: Use the module alias, not specific imports
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_rag_response(query: str, context: str | None = None) -> str:
    # 1. Prepare Context
    full_query = f"{context}\n\n{query}" if context else query
    print(f"DEBUG: Processing Query: {query}")

    # 2. Generate Embedding
    embedding = genai.embed_content(
        model="models/text-embedding-004", content=full_query
    )["embedding"]

    # 3. Search Qdrant (Hybrid Fix)
    # We try .search() (New). If it fails, we use .query_points() (Old)
    try:
        search_result = qdrant_client.search(
            collection_name=os.getenv("QDRANT_COLLECTION_NAME", "living_book_rag"),
            query_vector=embedding,
            limit=3,
        )
    except AttributeError:
        # Fallback for older Qdrant versions
        search_result = qdrant_client.query_points(
            collection_name=os.getenv("QDRANT_COLLECTION_NAME", "living_book_rag"),
            query=embedding,
            limit=3,
        )

    # 4. Extract Content (The "Tuple" Fix)
    # This loop handles Objects, Dictionaries, AND Tuples safely
    extracted_texts = []

    # Handle if search_result is wrapped in a tuple itself
    if isinstance(search_result, tuple):
        search_result = search_result[0] if search_result else []

    for hit in search_result:
        # Case A: It's a Tuple (Legacy Qdrant)
        if isinstance(hit, tuple):
            for item in hit:
                if hasattr(item, "payload") and item.payload:
                    extracted_texts.append(item.payload.get("content", ""))
                    break
                elif isinstance(item, dict) and "content" in item.get("payload", {}):
                    extracted_texts.append(item["payload"]["content"])
                    break
        # Case B: It's an Object (Modern Qdrant)
        elif hasattr(hit, "payload") and hit.payload:
            extracted_texts.append(hit.payload.get("content", ""))
        # Case C: It's a Dictionary
        elif isinstance(hit, dict) and "payload" in hit:
            extracted_texts.append(hit["payload"].get("content", ""))

    relevant_content = "\n\n".join(extracted_texts)
    print(f"DEBUG: Found {len(extracted_texts)} relevant chunks.")

    # 5. Synthesize Answer
    model = get_gemini_model()
    prompt = f"""You are a friendly and intelligent Technical Tutor for a book about Python.

        The user has highlighted a specific piece of text from the book and is asking for an explanation.

        1. **The User's Selection:** "{context if context else "None"}"
        2. **The Book Context (Surrounding paragraphs):**
        {relevant_content}

        **YOUR INSTRUCTIONS:**
        - Explain the "User's Selection" using the "Book Context" as your source of truth.
        - **CRITICAL:** If the User's Selection is a fragment (e.g., "In programmin"), a header (e.g., "Loops:"), or cut off, DO NOT say "context is incomplete." Instead, infer the full topic from the "Book Context" and explain that concept.
        - If the selection is "Loops:", explain what loops are based on the book.
        - Keep the answer concise and helpful for a beginner.

        User Question: {query}

        Answer:"""
    response = model.generate_content(prompt)

    return response.text
