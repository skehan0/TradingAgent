import httpx
import os
from datetime import datetime, timedelta
import dotenv
import logging

logger = logging.getLogger(__name__)

dotenv.load_dotenv()

def get_ai_news_articles() -> str:
    """Fetch AI-related news from yesterday"""
    
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        logger.error("No NEWS_API_KEY found in environment")
        return "No news API key configured"
    
    # Get yesterday's date in the required format
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    params = {
        'apiKey': api_key,
        'q': 'AI OR "artificial intelligence" OR "machine learning" OR ChatGPT OR OpenAI',
        'from': yesterday,
        'to': yesterday,
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 10
    }
    
    try:
        response = httpx.get('https://newsapi.org/v2/everything', params=params)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            if not articles:
                return "No AI news articles found"
            
            # Format articles for analysis
            news_text = []
            for i, article in enumerate(articles[:5], 1):  # Limit to top 5
                title = article.get('title', 'No title')
                description = article.get('description', 'No description')
                url = article.get('url', '')
                
                news_text.append(f"{i}. {title}\n   {description}\n   {url}\n")
            
            return "\n".join(news_text)
        else:
            logger.error(f"Error fetching news from API: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return f"Error fetching news: {response.status_code}"
            
    except Exception as e:
        logger.error(f"Error fetching news: {str(e)}")
        return f"Error fetching news: {str(e)}"