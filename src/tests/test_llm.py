from unittest.mock import Mock, patch

from src.services.llm import create_llm_response


def test_create_llm_response_with_valid_input():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
    mock_message = Mock()
    mock_message.content = "mock response"
    mock_choice = Mock()
    mock_choice.message = mock_message
    mock_response = Mock()
    mock_response.choices = [mock_choice]

    with patch("src.services.llm.ollama_client.chat.completions.create", return_value=mock_response):
        response = create_llm_response(messages)

    assert response == "mock response"