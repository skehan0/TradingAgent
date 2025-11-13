from typing import Any, Dict
from .news import get_ai_news_articles
from .llm import llm
from langsmith import traceable

@traceable
def llm_analysis(state: Dict[str, Any]) -> str:
    """Analyze AI news articles using LLM"""
    
    system_prompt = """You are a financial analyst specializing in AI/technology stocks. 
    
    Your task is to analyze AI-related news articles and provide actionable investment insights.
    
    For each significant article, provide:
    1. Key takeaways for investors
    2. Potential stock impact (bullish/bearish/neutral)
    3. Risk assessment
    4. Investment recommendations
    
    Focus on:
    - Major AI company announcements
    - Regulatory changes affecting AI
    - Market sentiment shifts
    - Competitive dynamics
    - Technology breakthroughs
    
    Return your analysis in a clear, actionable format suitable for trading decisions.
    Prioritise the top 10 most market-relevant articles.

    Example output format:
{
    "market_summary": "Brief overview of AI sector today",
    "top_opportunities": [
    {
      "ticker": "NVDA",
      "action": "BUY",
      "confidence": "HIGH",
      "reasoning": "Earnings beat, new AI chip launch",
      "price_target": 520,
      "timeframe": "1-2 weeks",
      "risk_level": "MEDIUM"
    }
  ],
  "top_risks": [
    {
      "ticker": "META",
      "concern": "Regulatory scrutiny on AI models",
      "impact": "BEARISH",
      "severity": "MEDIUM"
    }
  ],
  "sector_sentiment": {
    "semiconductors": "BULLISH",
    "software": "NEUTRAL",
    "cloud": "BULLISH"
  },
  "key_events": ["NVDA earnings call 2PM ET", "Fed AI regulation hearing"]
}
"""
    try:
        # Get news articles
        articles = get_ai_news_articles()
        
        if not articles:
            return "No AI news articles found for analysis."
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Analyze these AI news articles: {articles}"}
        ]
        
        analysis = llm.invoke(messages)
        return analysis
        
    except Exception as e:
        return f"Error during analysis: {str(e)}"