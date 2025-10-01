import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Configuration from environment variables
API_KEY = os.getenv("MAILGUN_API_KEY")
DOMAIN = os.getenv("MAILGUN_DOMAIN")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_analysis_report(analysis: str, articles_count: int = 0):
    """Send analysis report via email"""
    
    if not API_KEY:
        print("No API key found. Set API_KEY in .env")
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
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
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
            print(f"Email failed: {response.status_code}")
            return {"success": False}
            
    except Exception as e:
        print(f"Email error: {e}")
        return {"success": False}