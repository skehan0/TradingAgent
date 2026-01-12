import os
from dotenv import load_dotenv
from pkg_resources import Environment

from src.config.settings import Settings

def load_settings() -> Settings:
    load_dotenv()
    
    env = os.getenv("ENVIRONMENT", "development")
    
    # Validation - what if NEWS_API_KEY is missing?
    news_api_key = os.getenv("NEWS_API_KEY")
    if not news_api_key:
        raise ValueError("NEWS_API_KEY not set!")
    
    return Settings(
        environment=Environment(env),
        debug=env == "development",
        news_api_key=news_api_key,
        llm_api_key=os.getenv("LLM_API_KEY"),
        mailgun_api_key=os.getenv("MAILGUN_API_KEY"),
        mailgun_domain=os.getenv("MAILGUN_DOMAIN"),
        email_recipient=os.getenv("RECIPIENT_EMAIL"),
        email_sender=os.getenv("EMAIL_SENDER"),
    )   