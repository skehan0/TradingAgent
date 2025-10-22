from src.portfolio import Portfolio

def test_portfolio_value_calculation():
    portfolio = Portfolio()
    portfolio.buy("AAPL", 150.0, 10)  # Buy 10 shares at $150 each
    portfolio.buy("GOOGL", 1000.0, 5)  # Buy 5 shares at $1000 each
    
    current_prices = {
        "AAPL": 160.0,   # Current price of AAPL
        "GOOGL": 1100.0  # Current price of GOOGL
    }
    
    total_value = portfolio.portfolio_value(current_prices)
    expected_value = portfolio.cash + (10 * 160.0) + (5 * 1100.0)
    
    assert total_value == expected_value