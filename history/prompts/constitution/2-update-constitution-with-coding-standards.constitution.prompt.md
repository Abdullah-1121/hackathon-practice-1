---
id: 2
title: Update Constitution with Coding Standards
stage: constitution
date: 2025-11-25
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["governance", "coding-standards", "architecture"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

```
# 🏛️ Improved Project Constitution

## 3. Coding Standards & Quality Gates

### 🐍 Python Backend (FastAPI/Qdrant) Protocol
* **Data Validation (Crucial):**
    * Do NOT use raw dictionaries for API data. Use **Pydantic Models** for all request/response bodies.
    * *Bad:* `def chat(data: dict):`
    * *Good:* `class ChatRequest(BaseModel): query: str` -> `async def chat(request: ChatRequest):`
* **Async By Default:**
    * All route handlers MUST use `async def` to prevent blocking the server during Qdrant/Gemini API calls.
* **No Magic Strings:**
    * Never hardcode collection names or model names. Use constants at the top of the file.
    * *Bad:* `client.search(collection_name="my_books", ...)`
    * *Good:* `COLLECTION_NAME = "python_books_v1"` -> `client.search(collection_name=COLLECTION_NAME, ...)`

### ⚛️ React Frontend (Docusaurus) Protocol
* **Browser Safety (The Docusaurus Rule):**
    * Docusaurus builds server-side. You CANNOT access `window` or `document` directly in the main body of a component.
    * *Rule:* All DOM access (like selection search) MUST be wrapped in `useEffect` or `if (typeof window !== 'undefined')`.
* **Component Purity:**
    * Do not use Class Components. Use **Functional Components** with Hooks (`useState`, `useEffect`).
    * Separate logic from UI: Create a custom hook `useChatKit()` for the logic, and keep `ChatWidget.js` for the UI.

### 🛡️ AI & Security Protocol
* **Defensive API Calls:**
    * Every call to Google Gemini or Qdrant MUST be wrapped in a `try/except` block.
    * If the API fails, return a clean JSON error (e.g., `{\"error\": \"AI Brain is tired\"}`), do not crash the server.
* **Rate Limit Protection:**
    * When indexing the book (Looping through chapters), you MUST include `time.sleep(1)` between embedding calls to satisfy Free Tier limits.
```

## Response snapshot

```
The project constitution has been updated to version 1.1.0. This is a MINOR version bump due to the addition of detailed coding standards for the Python backend, React frontend, and AI & Security protocols.

Files flagged for manual follow-up to ensure consistency with the updated constitution:
- .specify/templates/plan-template.md
- .specify/templates/spec-template.md
- .specify/templates/tasks-template.md
- .specify/templates/commands/sp.constitution.md

Suggested commit message:
docs: amend constitution to v1.1.0 (add coding standards for frontend, backend, and AI/security)
```

## Outcome

- ✅ Impact: Project constitution updated with comprehensive coding standards.
- 🧪 Tests: N/A
- 📁 Files: 1 file modified: .specify/memory/constitution.md
- 🔁 Next prompts: Review and update other templates as per Sync Impact Report.
- 🧠 Reflection: Successfully updated constitution with new coding standards, ensuring clear guidelines for different parts of the project. Created a PHR for this update.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
