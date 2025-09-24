from openai import OpenAI
from langsmith.wrappers import wrap_openai
import os
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()

# Using Perplexity API
perplexity_client = wrap_openai(OpenAI(
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
))

@traceable
def create_llm_response(messages: list, model: str = "sonar", use_perplexity: bool = True) -> str:
    """Create LLM response using either Perplexity or OpenAI"""
    
    client = perplexity_client
    model_name = model
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.1,  # Low temperature for consistent financial analysis
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Simple interface for your analysis
class LLM:
    """Simple LLM wrapper for consistent interface"""
    
    def __init__(self, use_perplexity: bool = True, model: str = "sonar"):
        self.use_perplexity = use_perplexity
        self.model = model
    
    @traceable
    def invoke(self, messages: list) -> str:
        """Invoke the LLM with messages"""
        return create_llm_response(messages, self.model, self.use_perplexity)

# Default LLM instance
llm = LLM(use_perplexity=True, model="sonar")
