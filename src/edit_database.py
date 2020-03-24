from tkinter import *
from src.db_handler import DBWriter


class EditScreen(Frame):

    def initialize_gui(self):
        games = StringVar(self)
        select_label = Label(self, text = "Select game").grid(row = 0, column = 0)
        menu = OptionMenu(self, games, *DBWriter("DB/questions.db").get_games())
        menu.config(fg="red",bg='deep sky blue')
        menu.grid(row=1, column=0)



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Edit data")
        self.pack()
        self.initialize_gui()
        self.mainloop()

if __name__ == "__main__":
    EditScreen().initialize_gui()