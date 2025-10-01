from typing import Any, Dict
from .news import get_ai_news_articles
from .llm import llm
from langsmith import traceable

@traceable
def llm_analysis(state: Dict[str, Any]) -> Dict[str, Any]:
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
    Prioritize the top 10 most market-relevant articles."""
    
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