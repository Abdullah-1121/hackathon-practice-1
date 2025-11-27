from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


@patch("src.api.main.get_rag_response")
def test_chat_endpoint_passing(mock_get_rag_response):
    mock_get_rag_response.return_value = (
        "Mocked RAG response for: test query with test context"
    )
    response = client.post(
        "/api/chat", json={"query": "test query", "context": "test context"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "role": "assistant",
        "content": "Mocked RAG response for: test query with test context",
    }


@patch("subprocess.run")
def test_index_endpoint_passing(mock_subprocess_run):
    mock_subprocess_run.return_value.check_returncode = (
        lambda: None
    )  # Simulate successful execution
    response = client.post("/api/index")
    assert response.status_code == 200
    assert response.json() == {"status": "Indexing started successfully"}
