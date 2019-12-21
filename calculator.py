import sys
from card import Card

suits = ['d', 'h', 's', 'c']
values = ['2','3','4','5','6','7','8','9','10','J','H','K','A']
hands_list = []
building_hand = []

# Validate input string to determine if we can create new card object
def valid_card(value, suit):
    if value in values and suit in suits:
        return True
    else:
        return False

# Print out the current hand being built, as well as the list of hands
def print_hands():
    print ('Current hand: ', building_hand)
    print ('Hands after new addition: ', hands_list)

# Build a hand and if the hand is complete, add it to the list of hands
def build_hand(card):
    global building_hand
    if len(building_hand) == 0 :
        building_hand.append(card)
    else: 
        building_hand.append(card)
        hands_list.append(building_hand)
        building_hand = []

def main():
    while(1):
        new_card = input("Enter a card (Format Like 2s/ Jd/ Ah), or exit to terminate: ")
        if new_card in ['Exit', 'exit']:
            sys.exit()
        else:
            value = new_card[0:len(new_card)-1]
            suit = new_card[-1]
            if valid_card(value, suit):
                card = Card(value, suit)
                build_hand(card)
            else:
                print('Invalid card format')
            print_hands()

if __name__== "__main__":
    main()
