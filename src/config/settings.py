from dataclasses import dataclass
from enum import Enum

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

@dataclass
class Settings:
    environment: Environment
    debug: bool
    news_api_key: str
    llm_api_key: str
    mailgun_api_key: str
    mailgun_domain: str
    email_recipient: str
    email_sender: str