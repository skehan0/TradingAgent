from unittest.mock import patch, Mock
from src.services.mailgun import send_analysis_report

def test_send_analysis_report_with_valid_input():
    # Mock the HTTP request so we don't actually call Mailgun
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Queued. Thank you."}
    
    with patch('requests.post', return_value=mock_response):
        analysis = "This is a test analysis."
        result = send_analysis_report(analysis, 5)
        assert isinstance(result, dict)
        assert result["success"] is True