import sys
from card import Card


while(1):
    new_card = input("Enter a card (Format Like 2s/ Jd/ Ah), or exit to terminate: ")
    if new_card in ['Exit', 'exit']:
        sys.exit()
    else:
        value = new_card[0:len(new_card)-1]
        suit = new_card[-1]
        card = Card(value, suit)
        print(card)

    
