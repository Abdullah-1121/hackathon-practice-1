# Tasks: The Living Book Project

**Input**: Design documents from `/specs/001-living-book-rag/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Backend tests using `pytest` are implicitly requested by the constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume this web app structure.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create base directories: `backend/src`, `backend/tests`, `frontend/`, `frontend/src`, `frontend/src/theme`, `frontend/tests`, `scripts`, `.github/workflows`
- [X] T002 Initialize backend Python project with `uv` and `fastapi[standard]` in `backend/pyproject.toml` (Use `rag-backend` skill)
- [X] T003 Initialize frontend Docusaurus project in `frontend/` and configure base settings (e.g., site title "Cybernetic Book Documentation") (Use `docusaurus-expert` skill)
- [X] T004 [P] Configure basic linting and formatting for both frontend and backend (`backend/.flake8`, `frontend/.eslintrc.js`)

**Checkpoint**: Base project structure and configuration are set up.

---

## Phase 1.5: Content Creation

**Purpose**: Populate the Docusaurus site with initial content.

- [X] T005 Delete default Docusaurus tutorial files in `frontend/docs/tutorial-basics/` and `frontend/docs/tutorial-guides/` (Use `ghost-writer` subagent)
- [X] T006 Generate "01-introduction.md" in `frontend/docs/` (Use `ghost-writer` subagent)
- [X] T007 Generate "02-variables.md" in `frontend/docs/` (Use `ghost-writer` subagent)
- [X] T008 Generate "03-loops.md" in `frontend/docs/` (Use `ghost-writer` subagent)

**Checkpoint**: Initial Docusaurus content has been created and organized.

---

## Phase 2: Foundational (Backend Core)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented (Use `rag-backend` skill)

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Create `backend/src/api/main.py` for FastAPI application
- [X] T010 Implement basic FastAPI app structure (import router, create app instance) in `backend/src/api/main.py`
- [X] T011 Implement Qdrant client connection utility in `backend/src/services/qdrant_client.py` (Use `rag-backend` skill)
- [X] T012 Implement Google Gemini embedding client utility in `backend/src/services/gemini_client.py`
- [X] T013 Create base Pydantic models for request/response in `backend/src/models/` (e.g., `Message`, `ChatRequest`)

**Checkpoint**: Foundational backend services are ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Read with AI Context (Priority: P1) 🎯 MVP

**Goal**: Enable users to highlight text and receive AI explanations from the book.

**Independent Test**: A user can navigate to any chapter, highlight text, click the FAB, and receive an AI explanation of the selected context, pre-filling the chat input.

### Implementation for User Story 1

- [X] T014 [P] [US1] Swizzle Docusaurus Root component at `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T015 [P] [US1] Implement global `mouseup` event listener in `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T016 [P] [US1] Implement logic to detect text selection (`window.getSelection().toString()`) in `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T017 [P] [US1] Implement rendering of Floating Action Button (FAB) near mouse cursor when text is selected in `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T018 [US1] Implement FAB click handler to open ChatKit widget and inject selected text as context in `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T019 [US1] Implement pre-filling ChatKit user input with "Explain this context: ..." in `frontend/src/theme/Root.js` (Use `docusaurus-expert` skill)
- [X] T020 [US1] Implement `/api/chat` endpoint (POST) in `backend/src/api/main.py` to handle RAG requests (Use `rag-backend` skill)
- [X] T021 [US1] Implement RAG logic to receive user query + optional selected text in `backend/src/services/rag_service.py` (Use `rag-backend` skill)
- [X] T022 [US1] Implement RAG logic to convert query/text to vector using Google Gemini in `backend/src/services/rag_service.py` (Use `rag-backend` skill)
- [X] T023 [US1] Implement RAG logic to query Qdrant for top 3 relevant book chunks in `backend/src/services/rag_service.py` (Use `rag-backend` skill)
- [X] T024 [US1] Implement RAG logic to synthesize final answer using LLM in `backend/src/services/rag_service.py` (Use `rag-backend` skill)

**Checkpoint**: User Story 1 (Read with AI Context) is fully functional and testable independently.

---

## Phase 4: User Story 2 - General Book Chat (Priority: P2)

**Goal**: Enable users to ask general questions about the book's content at any time.

**Independent Test**: A user can open the ChatKit widget and ask a question about any topic covered in the book, receiving a relevant answer.

### Implementation for User Story 2

- [X] T025 [US2] Ensure ChatKit widget can be opened for general queries (e.g., via a static button, if not already handled by T018) in `frontend/src/components/ChatWidgetToggle.js` (Use `docusaurus-expert` skill)
- [X] T026 [US2] Ensure `/api/chat` endpoint in `backend/src/api/main.py` and `backend/src/services/rag_service.py` correctly handles general queries (without selected text) (Use `rag-backend` skill)

**Checkpoint**: User Stories 1 AND 2 are both functional and testable independently.

---

## Phase 5: User Story 3 - Browse Docusaurus Content (Priority: P3)

**Goal**: Allow users to easily navigate through the book's chapters and content.

**Independent Test**: A user can browse through all static Docusaurus pages, use the sidebar and navbar for navigation, and see the chat widget remain persistent.

### Implementation for User Story 3

- [X] T027 [US3] Configure Docusaurus sidebar to autogenerate from `/docs` in `frontend/docusaurus.config.js` (Use `docusaurus-expert` skill)
- [X] T028 [US3] Configure Docusaurus navbar with links to "Chapters", "About", and "GitHub Repo" in `frontend/docusaurus.config.js` (Use `docusaurus-expert` skill)
- [X] T029 [US3] Apply custom color scheme (e.g., #2e8555) in `frontend/src/css/custom.css` (Use `docusaurus-expert` skill)
- [X] T030 [US3] Verify ChatKit widget persistence across navigation (already implicitly handled by `Root.js` swizzling in T014) - *No additional code needed, just verification.*

**Checkpoint**: All user stories are independently functional and testable.

---

## Phase 6: Data Pipeline (Librarian Script)

**Purpose**: Index the book's content into Qdrant for RAG. (Use `rag-backend` skill)

- [X] T031 Create `scripts/index_book.py` script
- [X] T032 Implement scanning of `.md` files in `/docs` within `scripts/index_book.py`
- [X] T033 Implement text chunking by headers (##) or paragraphs (approx 500 tokens) in `scripts/index_book.py`
- [X] T034 Implement Google Gemini API calls for embedding with `time.sleep(1)` rate limiting in `scripts/index_book.py`
- [X] T035 Implement upserting vectors + metadata (Chapter Title, Page URL) to Qdrant in `scripts/index_book.py`
- [X] T036 Implement `/api/index` admin endpoint (POST) in `backend/src/api/main.py` to trigger the `index_book.py` script (Use `rag-backend` skill)

**Checkpoint**: The data pipeline is complete and the book can be indexed.

---

## Phase 7: Deployment

**Purpose**: Automate deployment to GitHub Pages.

- [X] T037 Create `.github/workflows/deploy.yml` for GitHub Actions
- [X] T038 Configure `deploy.yml` to build Docusaurus (`npm run build`) on push to `main`
- [X] T039 Configure `deploy.yml` to deploy to `gh-pages` branch on push to `main`

**Checkpoint**: Deployment workflow is set up and ready.

---

## Phase 8: Testing (Backend)

**Purpose**: Implement unit and integration tests for backend components using `pytest`.

- [X] T040 Write failing `pytest` for `/api/chat` endpoint in `backend/tests/test_api.py` (Use `rag-backend` skill)
- [X] T041 Implement passing test for `/api/chat` endpoint (Use `rag-backend` skill)
- [X] T042 Write failing `pytest` for `/api/index` endpoint in `backend/tests/test_api.py` (Use `rag-backend` skill)
- [X] T043 Implement passing test for `/api/index` endpoint (Use `rag-backend` skill)
- [X] T044 Write failing `pytest` for `rag_service.py` with context in `backend/tests/test_rag_service.py` (Use `rag-backend` skill)
- [X] T045 Implement passing test for `rag_service.py` with context (Use `rag-backend` skill)
- [X] T046 Write failing `pytest` for `rag_service.py` without context in `backend/tests/test_rag_service.py` (Use `rag-backend` skill)
- [X] T047 Implement passing test for `rag_service.py` without context (Use `rag-backend` skill)

**Checkpoint**: All backend functionalities have corresponding `pytest` tests.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Data Pipeline (Phase 6)**: Depends on Foundational phase completion
- **Deployment (Phase 7)**: Depends on all desired user stories being complete and data pipeline being available.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- T004 can run in parallel with T002 and T003.
- Frontend tasks (T010-T015) can be developed in parallel with Backend tasks (T016-T020) for User Story 1, once Foundational tasks are complete.
- Different user stories can be worked on in parallel by different team members.

---

## Parallel Example: User Story 1

```bash
# Frontend (docusaurus-expert skill):
Task: "Swizzle Docusaurus Root component at frontend/src/theme/Root.js"
Task: "Implement global mouseup event listener in frontend/src/theme/Root.js"
Task: "Implement logic to detect text selection in frontend/src/theme/Root.js"
Task: "Implement rendering of Floating Action Button (FAB) near mouse cursor in frontend/src/theme/Root.js"

# Backend (rag-backend skill):
Task: "Implement /api/chat endpoint (POST) in backend/src/api/main.py"
Task: "Implement RAG logic to receive user query + optional selected text in backend/src/services/rag_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Frontend + Backend parts)
   - Developer B: User Story 2 (Frontend + Backend parts)
   - Developer C: User Story 3 (Frontend parts)
3. Data Pipeline and Deployment can be handled concurrently or by a dedicated team member.
4. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
