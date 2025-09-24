"""
AI Trading Agent - Simple Entry Point
"""

from services.analysis import llm_node
from services.mailgun import send_analysis_report, test_email_service
from dotenv import load_dotenv

def main():
    """Simple main function"""
    load_dotenv()
    
    print("AI Trading Agent")
    
    # Run analysis
    result = llm_node({})
    
    if result.get('status') == 'complete':
        analysis = result.get('analysis', '')
        articles_count = result.get('articles_analyzed', 0)
        
        print(f"Analysis complete! ({articles_count} articles)")
        print("\n" + "="*50)
        print(analysis)
        print("="*50)
        
        email_result = send_analysis_report(analysis, articles_count)
        print(f"Email sent: {email_result.get('success', False)}")
        
    else:
        print(f"Analysis failed: {result.get('analysis', 'Unknown error')}")

if __name__ == "__main__":
    main()