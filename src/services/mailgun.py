"""
Simple email service using Mailgun
"""

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
AI Trading Analysis Report
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Articles Analyzed: {articles_count}

{analysis}

---
This is AI-generated analysis. Not financial advice.
    """.strip()
    
    # Send email
    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from": f"AI Trading Agent <postmaster@{DOMAIN}>",
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

def test_email_service():
    """Send a test email"""
    
    if not API_KEY:
        print("No API key found. Set API_KEY in .env")
        return {"success": False}
    
    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from": f"AI Trading Agent <postmaster@{DOMAIN}>",
                "to": RECIPIENT_EMAIL,
                "subject": "Test Email - Trading Agent",
                "text": "Test email from your AI Trading Agent. Everything is working!"
            }
        )
        
        if response.status_code == 200:
            print("Test email sent!")
            return {"success": True}
        else:
            print(f"Test email failed: {response.status_code}")
            return {"success": False}
            
    except Exception as e:
        print(f"Test email error: {e}")
        return {"success": False}

if __name__ == "__main__":
    # Test the email service
    print("Testing email service...")
    result = test_email_service()
    
    if result["success"]:
        print("Email sent successfully!")
        print(f"Message ID: {result.get('message_id')}")
        print(f"Recipients: {result.get('recipients')}")
    else:
        print("Email failed to send")
        print(f"Error: {result.get('error')}")