import sys
from tkinter import Tk, Button, Grid, Frame, N, E, S, W, PhotoImage
from card import Card


suits = ['d', 'h', 's', 'c']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hands_list = []
building_hand = []


class OddsCalculator():
    def __init__(self, master):
        self.master = master

        master.geometry("1000x400")
        master.resizable(width=False, height=False)
        master.title("Odds Calculator")

        frame = Frame(master)
        frame.grid(row=0, column=0, sticky=N+S+E+W)

        i = 0

        Grid.rowconfigure(master, 0, weight=1)
        Grid.columnconfigure(master, 0, weight=1)

        for row_index in range(len(suits)):
            suit = suits[row_index]
            Grid.rowconfigure(frame, row_index, weight=1)

            for col_index in range(len(values)):
                value = values[col_index]
                Grid.columnconfigure(frame, col_index, weight=1)
                self.button = Button(frame, text = value + " " + suit, command= lambda value = value, suit = suit : self.create_card(value, suit))
                # homescreenImage = PhotoImage(file="/Users/landonmarshall/Desktop/PacificHoldEmCalculator/Cards/" + value+suit.capitalize()+".jpg") 
                self.button.config(image = "/Users/landonmarshall/Desktop/PacificHoldEmCalculator/Cards/"+ value+suit.capitalize()+".jpg")
                self.button.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
        # for value in values:
        #     self.button = Button(master, text = value + "S", command= lambda value = value, suit = 's' : self.create_card(value, suit))
        #     self.button.grid(row = 0, column = i, columnspan=13, sticky=N+S+E+W)
        #     i = i + 1
        # for value in values:
        #     self.button = Button(master, text = value + "D", command= lambda value = value, suit = 's' : self.create_card(value, suit))
        #     self.button.grid(row = 1, column = i, columnspan=13, sticky=N+S+E+W)
        #     i = i + 1
        # self.twos = Button(master, text="Two S", command= lambda value = '2', suit = 's' : self.create_card(value, suit))
        # self.twos.grid(row=0, column=0, columnspan=13, sticky="we")
        # self.twod = Button(master, text="Two D", command= lambda value = '2', suit = 'd' : self.create_card(value, suit))
        # self.twod.grid(row=1, column=0, columnspan=13, sticky="we")

    def valid_card(self, value, suit):
        """ Validate input string to determine if input is valid card format """
        return value in values and suit in suits

    def create_card(self, value, suit):
        print(value + ' ' + suit)
        if self.valid_card(value, suit):
            card = Card(value, suit)
            self.build_hand(card)
        self.print_hands()
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

    # while(1):
    #     new_card = input("Enter a card (Format Like 2s/ Jd/ Ah), or exit to terminate: ")
    #     if new_card in ['Exit', 'exit']:
    #         sys.exit()
    #     else:
    #         value = new_card[0:len(new_card)-1]
    #         suit = new_card[-1]
    #         if valid_card(value, suit):
    #             card = Card(value, suit)
    #             build_hand(card)
    #         else:
    #             print('Invalid card format')
    #         print_hands()


if __name__ == "__main__":
    main()
