from unittest.mock import patch
from src.main import main

def test_main_sends_email_on_successful_analysis():
    with patch('src.main.llm_analysis', return_value="This is a test analysis."), \
         patch('src.main.send_analysis_report', return_value={"success": True}) as mock_send_email:
        main()
        mock_send_email.assert_called_once_with("This is a test analysis.", 0)