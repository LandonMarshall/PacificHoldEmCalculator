suits = {'d': 0, 'h': 1, 's': 2, 'c': 3}
values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'J': 11, 'Q': 12, 'K': 13, }

class Deck:
    def __init__(self):
        self.spades_available = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.clubs_available = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.diamonds_available = [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.hearts_available= [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.cards_array = [self.diamonds_available, self.hearts_available, \
            self.spades_available, self.clubs_available]
        self.deck_size = 52

    def __str__(self):
        return '           A  2  3  4  5  6  7  8  9  10 J  Q  K' + '\n' + \
               'Diamonds:  ' + '  '.join([str(elem) for elem in self.diamonds_available[1:]]) + '\n' + \
               'Hearts:    ' + '  '.join([str(elem) for elem in self.hearts_available[1:]]) + '\n' + \
               'Spades:    ' + '  '.join([str(elem) for elem in self.spades_available[1:]]) + '\n' + \
               'Clubs:     ' + '  '.join([str(elem) for elem in self.clubs_available[1:]]) + '\n' + \
               'Total cards left: ' + str(self.deck_size)
               
    def remove(self, card):
        if self.cards_array[suits[card.suit]][values[card.value]] == 1:
            self.cards_array[suits[card.suit]][values[card.value]] = 0
            self.deck_size -= 1
