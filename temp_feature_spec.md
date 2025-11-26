# Specification: The Death of Syntax

## 1. Product Overview
I want to build a Docusaurus 3.0 book titled **"The Death of Syntax: Why Specs Are the New Code"**.
This book explores the transition from Manual Coding to Spec-Driven Development (SDD) in the age of AI Agents.

## 2. The Book Content (Frontend)
The book must contain 3 core chapters in `/docs`:
1.  **"The Manual Era":** Discusses the inefficiencies of traditional coding (syntax errors, boilerplate, slow iteration).
2.  **"The Agentic Shift":** Explains how tools like Claude Code and Spec-Kit change the developer's role from "Writer" to "Reviewer".
3.  **"The Future Architecture":** A technical deep dive into how "Natural Language" (English) is becoming the highest-level programming language.

## 3. The RAG Chatbot (The "Debater")
* **Persona:** The chatbot should act as a "Futurist."
* **Feature:** Implementation of "Selection Search." If a user highlights a paragraph about "Manual Coding," they can ask the bot: *"Why is this inefficient?"*
* **Backend:** FastAPI + Qdrant Cloud.
* **Indexing:** Use the `rag-backend` skill to index these chapters using Gemini Embeddings.

## 4. Technical Constraints
* **Constraint 1:** Use the `docusaurus-expert` skill for all UI work.
* **Constraint 2:** Use the `rag-backend` skill for all API work.
* **Constraint 3:** The chat widget must be swizzled into the `Root` component.