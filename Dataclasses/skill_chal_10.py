
from dataclasses import dataclass
from functools import total_ordering
from typing import List

@dataclass(frozen=True)
class Stock:
    ticker: str
    price: float
    dividend: float = 0
    dividend_frequency: int = 4

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency

@dataclass
@total_ordering
class Position:
    stock: Stock
    shares: int

    def __lt__(self, other):
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.shares < other.stock.price * other.shares

    def __eq__(self, other):
        if type(other) != Position:
            raise TypeError("Can only compare instance of Position")

        return self.stock.price * self.shares == other.stock.price * other.shares

@dataclass
class Portfolio:
    holdings: List[Position]

    @property
    def value(self):
        total_value = sum([position.stock.price * position.shares for position in self.holdings])
        return total_value

    @property
    def portfolio_yield(self):
        total_dividends = sum([position.stock.annual_dividend * position.shares for position in self.holdings])

        return round((total_dividends / self.value), 6)


MSFT=Stock('MSFT',320,0.62,4) 
LMT=Stock('LMT',320,3.2,4)
GOOGLE=Stock('GOOGLE',2800,0,0) 
print(LMT.annual_dividend)
p1=Position(MSFT,100)
p2=Position(LMT,100)
p3=Position(GOOGLE,100)
print(p1==p2)
print(p3 <= p1)
Portfolio=Portfolio([p1,p2,p3])
print(Portfolio.portfolio_yield)
print(Portfolio.value)


