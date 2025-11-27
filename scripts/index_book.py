# scripts/index_book.py

import os
import re
import time
import uuid

import google.generativeai as genai
from dotenv import load_dotenv
from google.auth import load_credentials_from_dict
from qdrant_client import QdrantClient, models
from tomllib import load

load_dotenv()
# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Initialize Qdrant client
def get_qdrant_client():
    QDRANT_HOST = os.getenv("QDRANT_HOST")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    return QdrantClient(url=QDRANT_HOST, api_key=QDRANT_API_KEY)


def index_book_content():
    qdrant_client = get_qdrant_client()
    # Ensure collection exists
    collection_name = os.getenv("QDRANT_COLLECTION_NAME", "living_book_rag")
    try:
        qdrant_client.get_collection(collection_name=collection_name)
    except Exception:
        qdrant_client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=768, distance=models.Distance.COSINE
            ),
        )

    docs_path = "frontend/docs"
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Simple chunking by paragraph for now
                chunks = [
                    chunk.strip() for chunk in content.split("\n\n") if chunk.strip()
                ]

                points = []
                for i, chunk in enumerate(chunks):
                    if not chunk:
                        continue

                    # Generate embedding with rate limiting
                    time.sleep(1)
                    embedding = genai.embed_content(
                        model="models/text-embedding-004", content=chunk
                    )["embedding"]

                    # Extract metadata
                    title_match = re.search(r"^title: (.+)", content, re.MULTILINE)
                    chapter_title = (
                        title_match.group(1) if title_match else file.replace(".md", "")
                    )
                    page_url = f"/{os.path.relpath(filepath, 'frontend/docs').replace('.md', '')}"

                    points.append(
                        models.PointStruct(
                            id=str(
                                uuid.uuid5(uuid.NAMESPACE_DNS, f"{filepath}-{i}")
                            ),  # Unique ID for each chunk
                            vector=embedding,
                            payload={
                                "content": chunk,
                                "chapter_title": chapter_title,
                                "page_url": page_url,
                            },
                        )
                    )

                if points:
                    qdrant_client.upsert(collection_name=collection_name, points=points)
                    print(f"Indexed {len(points)} chunks from {filepath}")


if __name__ == "__main__":
    index_book_content()
