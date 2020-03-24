from tkinter import *
import sqlite3
import datetime

class AddData(Frame):

    def create_widgets(self):
        """Labels"""
        self.game_label = Label(self, text = "Game name").grid(row=0,column=0)
        self.edit_table = Button(self, text="Edit table").grid(row=1, column=0)
        self.quit = Button(self, command=self.quit_window,
                           text="Quit").grid(row=2,column=0)

        