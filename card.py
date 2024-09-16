
from tkinter import PhotoImage

class Card:
    def __init__(self, color, value) -> None:
        self.color = color
        self.value = value
        
        self.image_path = f"images\\{self.color}_{self.value}.png"
        self.image = PhotoImage(file=self.image_path)



    def __repr__(self):
        return f"Uno Card: {self.color} {self.value}"
    
    def compare(self, card):
        if self.color == card.color:
            print("They match colors")
        else:
            print("They don't match")


