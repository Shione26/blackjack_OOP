from deck_class import Deck
from person_class import Player, Dealer

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        print("\n----------------------------------------------------------------")
        print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
        print("                          Lets Play!")
        print("----------------------------------------------------------------")
        print("""
Game Rules:  Get as close to 21 as you can without going over!
        Dealer hits until he/she reaches 17.
        Aces count as 1 or 11.
        """)    

        for card_drawn in range(2):     # the player and dealer draws 2 cards from the deck
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)
        
    # function to print the cards before the result
    def show_some(self):
        print("Player's Hand:")
        print(" ", self.player.show_hand())
        print("Player's Hand =", self.player.hand_value())

        print("\nDealer's Hand:")
        print(" ", self.dealer.show_hand(hide_first=True))

    # function to print the cards for the final result
    def show_all(self):
        pass
