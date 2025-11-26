# Implementation Plan: The Living Book Project

**Branch**: `001-living-book-rag` | **Date**: 2025-11-26 | **Spec**: specs/001-living-book-rag/spec.md
**Input**: Feature specification from `/specs/001-living-book-rag/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This project aims to build a "Cybernetic Book," a Next-Gen documentation site using Docusaurus 3.0, enhanced with an embedded AI Agent. This agent will provide Retrieval-Augmented Generation (RAG) capabilities, allowing users to highlight text for explanations and ask general questions about the book's content. The backend will be developed with FastAPI, utilizing Qdrant Cloud for vector storage and Google Gemini for embeddings. The entire application will be deployed to GitHub Pages via a GitHub Actions workflow.

## Technical Context

**Language/Version**: Python 3.12+ (Backend), JavaScript/TypeScript (Frontend - Docusaurus uses React 18+)
**Primary Dependencies**: FastAPI, Qdrant Client, Google Generative AI, Docusaurus 3, React
**Storage**: Qdrant Cloud (Vector Database)
**Testing**: `pytest` (Backend), Frontend testing to be determined (e.g., Jest/React Testing Library for Docusaurus components)
**Target Platform**: Web application (Frontend deployed to GitHub Pages, Backend on localhost:8000 during development; future deployment TBD)
**Project Type**: Web application (Frontend + Backend)
**Performance Goals**: Users receive AI explanations within 5 seconds for 90% of requests; RAG backend correctly retrieves relevant chunks for 95% of queries.
**Constraints**: Google Gemini API rate limits (1 second sleep between embedding calls), Docusaurus server-side rendering limitations for DOM access.
**Scale/Scope**: Single documentation site, anticipated moderate user base. Indexing script designed for medium-sized books.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Test-Driven Development (TDD)**: Adhered. All new backend code will require failing `pytest` tests before implementation. Frontend testing strategy will be established.
- **The "Matrix" Protocol (CRITICAL)**: Adhered. Relevant skills (`docusaurus-expert`, `rag-backend`) will be loaded and followed during implementation phases.
- **Frontend: Docusaurus 3.0 (The Body)**: Adhered. Explicitly using Docusaurus 3 (React 18+), Infima/CSS Modules, Root component swizzling, and `window.getSelection()` for the killer feature.
- **Backend: FastAPI & RAG (The Mind)**: Adhered. Python 3.12+, FastAPI, Qdrant Cloud, Google Gemini (`text-embedding-004`), and `@dataclass` for models will be used.
- **Coding Standards & Quality Gates (General)**: Adhered. SOLID, DRY, KISS principles will be followed. All project files will be in Git.
- **🐍 Python Backend (FastAPI/Qdrant) Protocol**: Adhered. Pydantic models for API data, `async def` for route handlers, and constants for magic strings will be used.
- **⚛️ React Frontend (Docusaurus) Protocol**: Adhered. DOM access will be guarded with `useEffect` or `if (typeof window !== 'undefined')`. Functional components with hooks will be used, separating logic with a `useChatKit()` hook.
- **🛡️ AI & Security Protocol**: Adhered. `try/except` blocks for API calls, clean JSON error returns, and `time.sleep(1)` for rate limiting during indexing will be implemented.

All constitution gates are passed and adhered to.

## Project Structure

### Documentation (this feature)

```text
specs/001-living-book-rag/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── theme/           # For swizzled Root.js
│   └── services/
└── tests/

scripts/
└── index_book.py

.github/
└── workflows/
    └── deploy.yml
```

**Structure Decision**: The project will adopt a `web application` structure, with separate `backend/` and `frontend/` directories at the repository root. A `scripts/` directory will house the `index_book.py` data pipeline. GitHub Actions workflows will reside in `.github/workflows/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations detected that require justification.
