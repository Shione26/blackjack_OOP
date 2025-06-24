suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5,
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9,
    "10": 10, 
    "J": 10, 
    "Q": 10, 
    "K": 10, 
    "A": 11
}

class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self._rank} of {self._suit}"

    def get_rank(self):
        return self._rank
    
    def get_value(self):
        return values[self._rank]