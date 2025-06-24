from deck_class import Deck
from person_class import Player, Dealer
import time

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
        
        # player's turn
        while True:
            self.show_some()

            # checks if the player's card is above 21
            if self.player.hand_value() > 21:
                print("\n--- Player busts! ---")
                return
            
            # player's move
            move = input("\nWould you like to Hit or Stand? Enter [h/s] ").lower()
            if move == 'h':
                self.player.hit(self.deck)
            elif move == 's':
                print("Player stands. Dealer is playing.")
                break
            else:
                print("Sorry, Invalid Input. Please enter [h/s].")
    
        # dealer's turn
        while self.dealer.hand_value() < 17:    # by mechanics, the dealer does not play by strategy, thus must stand on 17
            self.dealer.hit(self.deck)

        time.sleep(1)
        print("\n----------------------------------------------------------------")
        print("                     ★ Final Results ★")
        print("----------------------------------------------------------------")

        self.show_all()
        self.evaluate_winner()

    # function to print the cards before the result
    def show_some(self):
        print("Player's Hand:")
        print(" ", self.player.show_hand())     # display player's cards
        print("Player's Hand =", self.player.hand_value())      # display player's cards value

        print("\nDealer's Hand:")
        print(" ", self.dealer.show_hand(hide_first=True))      # display dealer's cards except the first one

    # function to print the cards for the final result
    def show_all(self):
        print("\nPlayer's Hand:")
        print(" ", self.player.show_hand())     # display player's cards
        print("Player's Hand =", self.player.hand_value())      # display player's cards value

        print("\nDealer's Hand:")
        print(" ", self.dealer.show_hand())     # display dealer's cards
        print("Dealer's Hand =", self.dealer.hand_value())      # display dealer's cards value

    def evaluate_winner(self):
        player_value = self.player.hand_value()
        dealer_value = self.dealer.hand_value()

        if player_value > 21:
            print("\n--- Player busts! Dealer wins. ---")
        elif dealer_value > 21:
            print("\n--- Dealer busts! You win! ---")
        elif dealer_value > player_value:
            print("\n--- Dealer wins! ---")
        elif dealer_value < player_value:
            print("\n--- Player has blackjack! You win! ---")
        else:
            print("\nIts a tie!")
