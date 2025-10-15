from src.services.analysis import llm_analysis
from src.services.mailgun import send_analysis_report
from dotenv import load_dotenv

def main():
    """Simple main function"""
    load_dotenv()
    
    print("AI Trading Agent")
    
    # Run analysis
    analysis = llm_analysis({})
    
    if analysis and not analysis.startswith("Error") and not analysis.startswith("No AI"):
        print("Analysis complete!")
        print("\n" + "="*50)
        print(analysis)
        print("="*50)
        
        email_result = send_analysis_report(analysis, 0)
        print(f"Email sent: {email_result.get('success', False)}")
        
    else:
        print(f"Analysis failed: {analysis}")

if __name__ == "__main__":
    main()