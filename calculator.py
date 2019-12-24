import sys
import os
from tkinter import Tk, Button, Grid, Frame, PhotoImage, Image, Label
from Card import Card
from Deck import Deck


suits = ['d', 'h', 's', 'c']
suits_mapped = {'d': 0, 'h': 1, 's': 2, 'c': 3}
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values_mapped = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, }
hands_list = []
building_hand = []
deck = Deck()
odds_list = []


# TODO:
# Store suit and value as int instead of the chars

class OddsCalculator():
    def __init__(self, master):
        self.master = master
        self.images = {}
        master.geometry("1000x800")
        master.resizable(width=True, height=False)
        master.title("Odds Calculator")

        i,j = 0, 0



        card_frame = Frame(master, width=1000, height=400, pady=3)
        card_frame.grid(row=0, sticky="ne")


        self.output_frame = Frame(master, width=1000, height=400, pady=3)
        self.output_frame.grid(row=1, sticky="nsew")

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)


        # Create a button for each card on UI
        for row_index in range(len(suits)):
            suit = suits[row_index]
            card_frame.grid_rowconfigure(row_index, weight=1)
            for col_index in range(len(values)):
                value = values[col_index]
                card_frame.grid_columnconfigure(col_index, weight=1)
                self.images[value+ " " + suit] = PhotoImage(file= "2D.ppm")
                self.button = Button(card_frame,
                    text = value + "" + suit, 
                    width = 25,
                    height = 35,
                    fg =  '#ff0000' if row_index < 2 else '#000000',
                    # image = self.images[value+ " " + suit],
                    command= lambda value = value, 
                    suit = suit : self.create_card(value, suit))
                self.button.grid(row=row_index, column=col_index)  
        


    def update_output_GUI(self):
        """ Update GUI to show new stats for each hand"""



        for i in range(len(hands_list)):
            self.output_frame.grid_rowconfigure(i, weight=1)
            self.output_frame.grid_columnconfigure(3, weight=1)
            self.card_name_title = Label(self.output_frame, text = 'Hand', fg = '#000000')
            self.card_name_title.grid(row = 0, column = 0)
            
            self.pair_odds_title = Label(self.output_frame, text = 'Pair odds', fg = '#000000')
            self.pair_odds_title.grid(row = 0, column = 1)

            self.flush_odds_title = Label(self.output_frame, text = 'Flush odds', fg = '#000000')
            self.flush_odds_title.grid(row=0, column = 2)

            self.hand_label = Label(self.output_frame, fg = '#000000')
            self.hand_label['text'] = '%s, %s' % (hands_list[i][0], hands_list[i][1])
            self.hand_label.grid(row = i+1, column = 0)
            
            self.pair_odds_value = Label(self.output_frame, fg = '#000000')
            self.pair_odds_value['text'] = '%.5f' % odds_list[i]['pair_odds']
            self.pair_odds_value.grid(row = i+1, column = 1)

            self.flush_odds_value = Label(self.output_frame, fg = '#000000')
            
            self.flush_odds_value['text'] = '%.5f' % ((odds_list[i]['flush_odds']))
            self.flush_odds_value.grid(row = i+1, column = 2)

    def valid_card(self, value, suit):
        """ Validate input string to determine if input is valid card format """
        return value in values and suit in suits


    def create_card(self, value, suit):
        print(value + ' ' + suit)
        if self.valid_card(value, suit):
            card = Card(value, suit)
            self.print_hands()
            deck.remove(card)
            self.build_hand(card)
        else:
            print("Invalid card")
        print(deck)
        print (hands_list)
        print(odds_list)
        return


    def print_hands(self):
        """ Print out the current hand being built as well as the list of hands """
        print('Current hand: ', building_hand)
        print('Hands after new addition: ', hands_list)

    
    def build_hand(self, card):
        print ('----------------')
        print ('')
        """ Build a hand and if the hand is complete, add it to the list of hands """
        global building_hand

        if len(building_hand) == 0:
            building_hand.append(card)
        else:
            building_hand.append(card)
            hands_list.append(building_hand)
            odds_list.append({})
            building_hand = []
            self.pair_odds()
            self.flush_odds()

            self.update_output_GUI()

    def pair_odds(self):
        global hands_list
        i = 0
        
        for hand in hands_list:
            if hand[0].value == hand[1].value:
                odds_list[i]['pair_odds'] = 1
            else:
                pair_cards = 0
                for j in range(2):
                    for suit in suits:
                        if hand[j].suit != suit:
                            suit_map = suits_mapped[suit]
                            val_map = values_mapped[hand[j].value]
                            if deck.cards_array[suit_map][val_map] == 1: 
                                pair_cards += 1
                odds_list[i]['pair_odds'] = pair_cards/deck.deck_size
            i += 1
        
    def flush_odds(self):
        global hands_list
        i = 0
        cards_to_get = 4

        for hand in hands_list:
            if hand[0].suit == hand[1].suit:
                cards_to_get = 3
                cards_left_in_suit = deck.cards_array[suits_mapped[hand[0].suit]].count(1)
                if cards_left_in_suit >= 3:
                    # example: 7hearts/26 cards * 6hearts/25 cards * 5hearts/24 cards
                    # = chances of getting a flush
                    if i == 0:
                        print(cards_left_in_suit,deck.deck_size)
                    odds_list[i]['flush_odds'] = (cards_left_in_suit/deck.deck_size) * \
                    ((cards_left_in_suit - 1) /(deck.deck_size - 1)) * \
                    ((cards_left_in_suit - 2)/(deck.deck_size - 2))
                else: odds_list[i]['flush_odds'] = 0
            else:
                cards_to_get = 4
                cards_left_in_suit_a = deck.cards_array[suits_mapped[hand[0].suit]].count(1)
                if (cards_left_in_suit_a >= 4):
                    suit_a_odds = (cards_left_in_suit_a/deck.deck_size) * \
                    ((cards_left_in_suit_a - 1) /(deck.deck_size - 1)) * \
                    ((cards_left_in_suit_a - 2)/(deck.deck_size - 2)) * \
                    ((cards_left_in_suit_a - 3)/(deck.deck_size - 3))
                else:
                    suit_a_odds = 0
                cards_left_in_suit_b = deck.cards_array[suits_mapped[hand[1].suit]].count(1)
                if (cards_left_in_suit_b >= 4):
                    suit_b_odds = (cards_left_in_suit_b/deck.deck_size) * \
                    ((cards_left_in_suit_b - 1) /(deck.deck_size - 1)) * \
                    ((cards_left_in_suit_b - 2)/(deck.deck_size - 2)) * \
                    ((cards_left_in_suit_b - 3)/(deck.deck_size - 3))
                else:
                    suit_b_odds = 0
                odds_list[i]['flush_odds'] = suit_a_odds + suit_b_odds

            i += 1


def main():
    root = Tk()
    gui = OddsCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
