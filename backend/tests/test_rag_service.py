from unittest.mock import MagicMock, patch

import pytest

from src.services.rag_service import get_rag_response


@patch("src.services.rag_service.genai")
@patch("src.services.rag_service.qdrant_client")
@patch("src.services.rag_service.get_gemini_model")
def test_get_rag_response_with_context_passing(
    mock_get_gemini_model, mock_qdrant_client, mock_genai
):
    mock_genai.embed_content.return_value = {"embedding": [0.1] * 768}
    mock_qdrant_client.query_points.return_value = [
        MagicMock(payload={"content": "relevant chunk 1"}),
        MagicMock(payload={"content": "relevant chunk 2"}),
    ]
    mock_model = MagicMock()
    mock_model.generate_content.return_value.text = "Mocked RAG response for: What is this about? with context relevant chunk 1 relevant chunk 2"
    mock_get_gemini_model.return_value = mock_model

    query = "What is this about?"
    context = "This is some important context."
    response = get_rag_response(query, context)

    assert (
        response
        == "Mocked RAG response for: What is this about? with context relevant chunk 1 relevant chunk 2"
    )


@patch("src.services.rag_service.genai")
@patch("src.services.rag_service.qdrant_client")
@patch("src.services.rag_service.get_gemini_model")
def test_get_rag_response_without_context_passing(
    mock_get_gemini_model, mock_qdrant_client, mock_genai
):
    mock_genai.embed_content.return_value = {"embedding": [0.1] * 768}
    mock_qdrant_client.query_points.return_value = [
        MagicMock(payload={"content": "general relevant chunk"}),
    ]
    mock_model = MagicMock()
    mock_model.generate_content.return_value.text = "Mocked RAG response for: General question? without context general relevant chunk"
    mock_get_gemini_model.return_value = mock_model

    query = "General question?"
    response = get_rag_response(query)

    assert (
        response
        == "Mocked RAG response for: General question? without context general relevant chunk"
    )
