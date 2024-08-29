from random import choice
from dataclasses import dataclass
from itertools import product
@dataclass
class PlayingCard:
    suit: str
    rank: str
    def __post_init__(self):
        self.suit=self.suit.lower()
        self.rank=self.rank.lower()
    def __eq__(self,other):
        return self.suit==other.suit and self.rank==other.rank
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.suit}','{self.rank}')"
class CardDeck:
    def __init__(self, deck=None):
        self.i = 0
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        
        if deck is None:
            self.deck = [PlayingCard(*args)for args in product(self.suits, self.ranks)]
        else:
            valid_cards = self.deck = [PlayingCard(*args)for args in product(self.suits, self.ranks)]
            if all(isinstance(card, PlayingCard) and card in valid_cards for card in deck):
                self.deck = deck
            else:
                self.deck = self.deck = [PlayingCard(*args)for args in product(self.suits, self.ranks)]
    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.deck)})"
    def draw(self, n=1):
        if n == 1:
            drawn = choice(self.deck)
            self.deck.remove(drawn)
            return drawn
        else:
            drawn_cards = []
            for _ in range(n):
                if len(self.deck) == 0:
                    break
                drawn = choice(self.deck)
                self.deck.remove(drawn)
                drawn_cards.append(drawn)
            return CardDeck(drawn_cards)

    def __len__(self):
        return len(self.deck)
    def __getitem__(self,key):
        if type(key) == slice:
            return (self.deck[key])
        elif type(key) == int:
            return self.deck[key]
        return NotImplemented
    def __contains__(self,item):
        return item in self.deck
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.i+=1
            return self.deck[self.i-1]
        except IndexError:
            self.i=0
            raise StopIteration
    def __add__(self,other):
        if isinstance(other,PlayingCard):
            return CardDeck([*self.deck,other])
        return CardDeck(self.deck+other.deck)
    def __radd__(self, other):
        return self + other
    def __mul__(self,other):
        if isinstance(other,int):
            return CardDeck(self.deck*other)
    def __rmul__(self, other):
        return self * other

cd=CardDeck()
cd2=CardDeck([PlayingCard('hearts','2'),PlayingCard('diamonds','3')])
cd3=CardDeck([PlayingCard('hearts','5'),PlayingCard('spades','4')])
cd4=CardDeck([PlayingCard('hearts','5'),'pop'])
#print(cd)
print(cd2)
print(cd3)
print(cd4)
