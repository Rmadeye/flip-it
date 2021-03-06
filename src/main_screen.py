from tkinter import *
from src import frontend as f
from src import create_questions as cq

"""Main screen of the application"""


class MainScreen(Frame):

    def initialize_game(self):
        return f.Front(Toplevel())

    def initialize_questions(self):
        return cq.QuestionsFrontend(Toplevel())

    def quit_game(self):
        return quit()


    def initialize_gui(self):
        self.play_button = Button(self, command = self.initialize_game,
                                  text = "Play the game!").grid(row = 1, column = 0)
        self.edit_questions = Button(self, command = self.initialize_questions,
                                     text="Edit questions").grid(row=2, column=0)
        self.quit = Button(self, command=self.quit_game,
                           text="Quit").grid(row=3,column=0)
        """Welcome label"""
        text = "Welcome to flipquiz, game made to enhance people language skills. Feel free to use it! "
        """Welcome label"""
        self.welcome_label = Label(self, text=text).grid(row=0, column=0)



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initialize_gui()
        self.winfo_toplevel().title("Flip-it")
        self.mainloop()

if __name__ == "__main__":
    MainScreen()