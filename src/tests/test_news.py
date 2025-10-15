from src.services.news import get_ai_news_articles
import httpx
from unittest.mock import patch

def test_get_ai_news_articles_returns_list():
    articles = get_ai_news_articles()
    assert isinstance(articles, str)
    assert len(articles) > 0
    assert "No AI news articles found" not in articles

def test_get_ai_news_articles_handles_empty_response():
    class MockResponse:
        status_code = 200
        def json(self):
            return {"articles": []}

    with patch('httpx.get', return_value=MockResponse()):
        articles = get_ai_news_articles()
        assert articles == "No AI news articles found"


def test_get_ai_news_articles_handles_missing_api_key():
    with patch.dict('os.environ', {'NEWS_API_KEY': ''}):
        articles = get_ai_news_articles()
        assert articles == "No news API key configured"