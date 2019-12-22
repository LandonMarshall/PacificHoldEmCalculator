import sys
import os
from tkinter import Tk, Button, Grid, Frame, N, E, S, W, PhotoImage, Image
from Card import Card
from Deck import Deck


suits = ['d', 'h', 's', 'c']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
hands_list = []
building_hand = []
deck = Deck()

class OddsCalculator():
    def __init__(self, master):
        self.master = master
        self.images = {}
        master.geometry("1000x400")
        master.resizable(width=True, height=False)
        master.title("Odds Calculator")
        frame = Frame(master)
        frame.grid(row=0, column=0, sticky=N+S+E+W)
        i = 0

        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)

        # Create a button for each card on UI
        for row_index in range(len(suits)):
            suit = suits[row_index]
            Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(len(values)):
                value = values[col_index]
                Grid.columnconfigure(frame, col_index, weight=1)
                self.images[value+ " " + suit] = PhotoImage(file= "2D.ppm")
                self.button = Button(frame,
                    text = value + "" + suit, 
                    width = 25,
                    height = 35,
                    fg =  '#ff0000' if row_index < 2 else '#000000',
                    # image = self.images[value+" " + suit],
                    command= lambda value = value, 
                    suit = suit : self.create_card(value, suit))
                self.button.grid(row=row_index, column=col_index)  
                i = i + 1


    def valid_card(self, value, suit):
        """ Validate input string to determine if input is valid card format """
        return value in values and suit in suits


    def create_card(self, value, suit):
        print(value + ' ' + suit)
        if self.valid_card(value, suit):
            card = Card(value, suit)
            self.build_hand(card)
        self.print_hands()
        deck.remove(card)
        print(deck)
        return


    def print_hands(self):
        """ Print out the current hand being built as well as the list of hands """
        print('Current hand: ', building_hand)
        print('Hands after new addition: ', hands_list)

    
    def build_hand(self, card):
        """ Build a hand and if the hand is complete, add it to the list of hands """
        global building_hand

        if len(building_hand) == 0:
            building_hand.append(card)
        else:
            building_hand.append(card)
            hands_list.append(building_hand)
            building_hand = []


def main():
    root = Tk()
    gui = OddsCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
