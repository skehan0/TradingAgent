from unittest.mock import patch
from src.services.analysis import llm_analysis

def test_llm_analysis_returns_error_when_no_articles():
    with patch('src.services.analysis.get_ai_news_articles', return_value=[]):
        result = llm_analysis({})  # Empty dict because that's what the function expects
        assert result == "No AI news articles found for analysis."