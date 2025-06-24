suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank