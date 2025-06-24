import random
from card_class import Card

suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

class Deck:
    def __init__(self): 
        self._cards = []    # list to store 52 card objects
        for suit in suits:
            for rank in ranks:
                self._cards.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self._cards)