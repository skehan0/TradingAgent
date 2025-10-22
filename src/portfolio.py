class Portfolio:
    def __init__(self):
        self.cash = 10000.0  # Starting with $10,000
        self.holdings = {}   # Stock symbol to number of shares

    def buy(self, symbol: str, price: float, shares: int) -> bool:
        total_cost = price * shares
        if total_cost > self.cash:
            return False  # Not enough cash to buy
        self.cash -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + shares
        return True

    def sell(self, symbol: str, price: float, shares: int) -> bool:
        total_sales = price * shares
        if symbol not in self.holdings or self.holdings[symbol] < shares:
            return False  # Not enough shares to sell
        self.cash += total_sales
        self.holdings[symbol] -= shares
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        return True
    
    def hold(self, symbol: str, shares: int) -> bool:
        if symbol not in self.holdings or self.holdings[symbol] < shares:
            return False  # Not enough shares to hold
        # Holding does not change cash or holdings
        return True
    
    def portfolio_value(self, current_prices: dict) -> float:
        total_value = self.cash
        for symbol, shares in self.holdings.items():
            total_value += current_prices.get(symbol, 0) * shares
        return total_value
    
    def get_holdings(self) -> dict:
        return self.holdings.copy()