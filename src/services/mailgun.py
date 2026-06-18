import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Configuration from environment variables
API_KEY = os.getenv("MAILGUN_API_KEY")
DOMAIN = os.getenv("MAILGUN_DOMAIN")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
BASE_URL = os.getenv("MAILGUN_BASE_URL", "https://api.mailgun.net/v3")


def _is_sandbox_domain(domain: str | None) -> bool:
    return bool(domain) and domain.startswith("sandbox")


def _is_recipient_authorized() -> bool:
    if not _is_sandbox_domain(DOMAIN):
        return True

    try:
        response = requests.get(
            f"https://api.mailgun.net/v5/{DOMAIN}/auth_recipients",
            params={"email": RECIPIENT_EMAIL},
            auth=("api", API_KEY),
        )
        data = response.json() if response.content else {}
        return bool(data.get("recipient", {}).get("activated", False))
    except Exception:
        return False

def send_analysis_report(analysis: str, articles_count: int = 0):
    """Send analysis report via email"""
    
    if not API_KEY:
        print("No MAILGUN_API_KEY found in .env")
        return {"success": False}

    if not DOMAIN:
        print("No MAILGUN_DOMAIN found in .env")
        return {"success": False}

    if not RECIPIENT_EMAIL:
        print("No RECIPIENT_EMAIL found in .env")
        return {"success": False}

    if not _is_recipient_authorized():
        print(
            "Mailgun sandbox recipient is not activated. "
            "Authorize the recipient in Mailgun before sending from a sandbox domain."
        )
        return {"success": False}
    
    # Create email content
    content = f"""
Tradeskee AI Agent Analysis Report
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Articles Analyzed: {articles_count}

{analysis}

---
This is AI-generated analysis. Not financial advice.
    """
    
    # Send email
    try:
        response = requests.post(
            f"{BASE_URL}/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from": f"Tradeskee AI Trading Agent <postmaster@{DOMAIN}>",
                "to": RECIPIENT_EMAIL,
                "subject": f"Trading Analysis - {datetime.now().strftime('%B %d')}",
                "text": content
            }
        )
        
        if response.status_code == 200:
            print("Email sent successfully!")
            return {"success": True}
        else:
            print(f"Email failed: {response.status_code} - {response.text}")
            return {"success": False}
            
    except Exception as e:
        print(f"Email error: {e}")
        return {"success": False}