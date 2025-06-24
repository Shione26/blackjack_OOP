from hand_class import Hand

class Person:
    def __init__ (self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        card = deck.deal()          # take a card from the deck
        self.hand.add_card(card)    # add it to the person's hand
        return card