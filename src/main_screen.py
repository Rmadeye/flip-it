from tkinter import *
from src import frontend as f

"""Main screen of the application"""


class MainScreen:



    def __init__(self):
        self.screen = Tk()
        self.screen.wm_title("Welcome to Flip The Buttons!")
        """Welcome label"""
        text = "Welcome to flipquiz, game made to enhance people language skills. Feel free to use it! "
        self.welcome_label = Label(self.screen, text = text).grid(row = 0, column = 0)

        def initialize_game():
            return f.Front()

        def initialize_questions():
            return None

        self.play_button = Button(self.screen, command = initialize_game, text = "Play the game!").grid(row = 1, column = 0)
        self.edit_questions = Button(self.screen, command = initialize_questions, text="Edit questions").grid(row=2, column=0)








        self.screen.mainloop()
if __name__ == "__main__":
    MainScreen()