<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0 (MAJOR: Initial version or significant overhaul)
List of modified principles:
  - PROJECT_NAME -> The Cybernetic Book Protocol
  - PRINCIPLE_1_NAME -> Test-Driven Development (TDD)
  - PRINCIPLE_1_DESCRIPTION -> You MUST write a failing test (pytest) before writing implementation code. No code exists without a test.
  - PRINCIPLE_2_NAME -> The "Matrix" Protocol (CRITICAL)
  - PRINCIPLE_2_DESCRIPTION -> Before writing ANY code, check `.claude/skills/` for relevant skills.
* If a Skill exists (e.g., `docusaurus-expert` or `rag-backend`), you MUST load it and strictly follow its instructions.
* **Violation of this rule is a critical failure.** Do not "guess" implementation details if a Skill defines them.
  - SECTION_2_NAME -> Technology Stack & Constraints
  - SECTION_2_CONTENT -> ### 🟢 Frontend: Docusaurus 3.0 (The Body)
* **Framework:** Docusaurus 3 (React 18+).
* **Styling:** Infima (Default) + Custom CSS Modules.
* **Chat Integration:**
* Must use **Swizzling** on the `Root` component to persist the chat widget across page navigation.
* **Killer Feature:** The frontend MUST capture `window.getSelection()` and pass it to the ChatKit context for "Search by Selection".

### 🔵 Backend: FastAPI & RAG (The Mind)
* **Language:** Python 3.12+ (Use `uv` for package management).
* **API Framework:** FastAPI (`fastapi[standard]`).
* **Vector DB:** Qdrant Cloud (Free Tier).
* **Embeddings:** Google Gemini (`text-embedding-004`) via `google-generativeai`.
* **Data Structures:** Use `@dataclass` for all internal data models.
  - SECTION_3_NAME -> Coding Standards & Quality Gates
  - SECTION_3_CONTENT -> ### General
* **Clean Code:** Follow SOLID, DRY, and KISS principles.
* **Git:** Keep all project files in git.
  - GOVERNANCE_RULES -> This constitution supersedes all other practices; Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance; Complexity must be justified.
  - CONSTITUTION_VERSION -> 1.0.0
  - RATIFICATION_DATE -> 2025-11-25
  - LAST_AMENDED_DATE -> 2025-11-25
Added sections: None (existing sections filled)
Removed sections: PRINCIPLE_3_NAME, PRINCIPLE_3_DESCRIPTION, PRINCIPLE_4_NAME, PRINCIPLE_4_DESCRIPTION, PRINCIPLE_5_NAME, PRINCIPLE_5_DESCRIPTION, PRINCIPLE_6_NAME, PRINCIPLE__DESCRIPTION from template.
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/sp.constitution.md ⚠ pending
Follow-up TODOs: None
-->
<!--
Sync Impact Report:
Version change: 1.0.0 -> 1.1.0 (MINOR: Added detailed coding standards)
List of modified principles:
  - Added "🐍 Python Backend (FastAPI/Qdrant) Protocol" section
  - Added "⚛️ React Frontend (Docusaurus) Protocol" section
  - Added "🛡️ AI & Security Protocol" section
Added sections: None (existing sections updated)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/sp.constitution.md ⚠ pending
Follow-up TODOs: None
-->
# The Cybernetic Book Protocol Constitution

## Core Principles

### Test-Driven Development (TDD)
You MUST write a failing test (pytest) before writing implementation code. No code exists without a test.

### The "Matrix" Protocol (CRITICAL)
* Before writing ANY code, check `.claude/skills/` for relevant skills.
* If a Skill exists (e.g., `docusaurus-expert` or `rag-backend`), you MUST load it and strictly follow its instructions.
* **Violation of this rule is a critical failure.** Do not "guess" implementation details if a Skill defines them.

## Technology Stack & Constraints

### 🟢 Frontend: Docusaurus 3.0 (The Body)
* **Framework:** Docusaurus 3 (React 18+).
* **Styling:** Infima (Default) + Custom CSS Modules.
* **Chat Integration:**
* Must use **Swizzling** on the `Root` component to persist the chat widget across page navigation.
* **Killer Feature:** The frontend MUST capture `window.getSelection()` and pass it to the ChatKit context for "Search by Selection".

### 🔵 Backend: FastAPI & RAG (The Mind)
* **Language:** Python 3.12+ (Use `uv` for package management).
* **API Framework:** FastAPI (`fastapi[standard]`).
* **Vector DB:** Qdrant Cloud (Free Tier).
* **Embeddings:** Google Gemini (`text-embedding-004`) via `google-generativeai`.
* **Data Structures:** Use `@dataclass` for all internal data models.

## Coding Standards & Quality Gates

### General
* **Clean Code:** Follow SOLID, DRY, and KISS principles.
* **Git:** Keep all project files in git.

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

## Governance
This constitution supersedes all other practices; Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance; Complexity must be justified.

**Version**: 1.1.0 | **Ratified**: 2025-11-25 | **Last Amended**: 2025-11-25
