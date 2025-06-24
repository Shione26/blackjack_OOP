class Hand:
    def __init__(self):
        self._cards = []
        self._value = 0     # initialize value to track total hand value
        self._aces = 0      # initialize aces to track Aces 

    def add_card(self, card):
        self._cards.append(card)    # add card to cards list
        self._value += card.get_value()     # add card's value to get_value()
        if card.get_rank() == "A":  
            self._aces += 1     # increment Ace if the card is ace
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self._value > 21 and self._aces:      # adjust the ace's value if it exceeds 21
            self._value -= 10       # make ace value from 11 to 1
            self._aces -= 1     # decrement number of ace

    def get_cards(self):
        return self._cards

    def get_value(self):
        return self._value