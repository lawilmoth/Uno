import tkinter as tk
from tkinter import PhotoImage

from card import Card
from deck import Deck
window = tk.Tk()

game_deck = Deck()

def print_hello(card):
    print(card)



label = tk.Label(window, text="Hello")
label.grid(column=0,row=0)

for i, card in enumerate(game_deck.deck):
    
    button = tk.Button(
        window,
        command = lambda card=card: print_hello(card),
        image=card.image
    )

    button.grid(column=1,row=i)

window.mainloop()