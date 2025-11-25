---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-11-25
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["governance", "architecture"]
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
# 🏛️ Project Constitution: The Cybernetic Book Protocol

## 1. Prime Directives (Immutable)

1. **Test-Driven Development (TDD):** You MUST write a failing test (pytest) before writing implementation code. No code exists without a test.

2. **The "Matrix" Protocol (CRITICAL):**

* Before writing ANY code, check `.claude/skills/` for relevant skills.

* If a Skill exists (e.g., `docusaurus-expert` or `rag-backend`), you MUST load it and strictly follow its instructions.

* **Violation of this rule is a critical failure.** Do not "guess" implementation details if a Skill defines them.



## 2. Technology Stack & Constraints



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



## 3. Coding Standards & Quality Gates



### General

* **Clean Code:** Follow SOLID, DRY, and KISS principles.

* **Git:** Keep all project files in git.
```

## Response snapshot

```
The project constitution has been updated to version 1.0.0. This is a MAJOR version bump due to the initial definition of core principles and technology stack.

Files flagged for manual follow-up to ensure consistency with the updated constitution:
- .specify/templates/plan-template.md
- .specify/templates/spec-template.md
- .specify/templates/tasks-template.md
- .specify/templates/commands/sp.constitution.md

Suggested commit message:
docs: amend constitution to v1.0.0 (initial principles, tech stack, and coding standards)
```

## Outcome

- ✅ Impact: Project constitution updated with core principles, tech stack, and coding standards.
- 🧪 Tests: N/A
- 📁 Files: 1 file modified: .specify/memory/constitution.md
- 🔁 Next prompts: Review and update other templates as per Sync Impact Report.
- 🧠 Reflection: Successfully updated constitution based on user input, ensuring all principles and technical guidelines are documented. Handled script failure by using agent-native tools for PHR creation.

## Evaluation notes (flywheel)

- Failure modes observed: PHR creation script not found.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure PHR creation script path is correct or directly use agent-native tools.
