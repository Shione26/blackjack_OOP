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
    
    def show(self, hide_first=False):   # if it's the player, shows all cards. If the dealer, hide the first card
        if hide_first:      # if hide_first is true, it will loop to just reveal the second card and hide the first card for the dealer
            card_strings = []       # list to store the string of each cards except the first one
            for card in self._cards[1:]:    
                card_strings.append(str(card))      # convert card to string and append to the list
            return "<card hidden>\n  " + " ".join(card_strings)
        else:       # else, list all cards normally for the player
            card_strings = []
            for card in self._cards:
                card_strings.append(str(card))
            return "\n  ".join(card_strings)