from openai import OpenAI
from langsmith.wrappers import wrap_openai
import os
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()

# Using Ollama's OpenAI-compatible API
ollama_client = wrap_openai(OpenAI(
    api_key=os.getenv("OLLAMA_API_KEY", "ollama"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
))

@traceable
def create_llm_response(messages: list, model: str = "gemma4:e4b", use_perplexity: bool = True) -> str:
    client = ollama_client
    model_name = model or os.getenv("OLLAMA_MODEL", "gemma4:e4b")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.1,  # Low temperature for consistent financial analysis
            max_tokens=2000
        )
        content = response.choices[0].message.content
        return content if content is not None else "No response generated"
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Simple interface for your analysis
class LLM:
    """Simple LLM wrapper for consistent interface"""
    
    def __init__(self, use_perplexity: bool = True, model: str = "gemma4:e4b"):
        self.use_perplexity = use_perplexity
        self.model = model
    
    @traceable
    def invoke(self, messages: list) -> str:
        """Invoke the LLM with messages"""
        return create_llm_response(messages, self.model, self.use_perplexity)

# Default LLM instance
llm = LLM(use_perplexity=False, model=os.getenv("OLLAMA_MODEL", "gemma4:e4b"))
