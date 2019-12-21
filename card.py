print_values = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10',
                'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}

print_suits = {'d': 'Diamonds', 'h': 'Hearts', 's': 'Spades', 'c': 'Clubs'}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return print_values[self.value] + " of " + print_suits[self.suit]

    def __repr__(self):
        return self.value + self.suit
