from src.services.llm import create_llm_response
import os


def test_create_llm_response_with_valid_input():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
    response = create_llm_response(messages)
    assert isinstance(response, str)
    assert len(response) > 0
    assert not response.startswith("Error")
    assert response != "No response generated"