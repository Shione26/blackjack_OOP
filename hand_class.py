class Hand:
    def __init__(self):
        self._cards = []
        self._value = 0     # initialize value to track total hand value

    def add_card(self, card):
        self._cards.append(card)    # add card to cards list
        self._value += card.get_value()     # add card's value to get_value()
