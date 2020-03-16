import sqlite3
from tkinter import *
from src import db_handler as db

class TableToolkitFrontend(Frame):



    def create_widgets(self):
        def add_question_row():
            self.question_counter += 1
            self.point_counter += 100
            if self.point_counter > 500:
                self.point_counter = 100
            self.question_label = Label(self, text = "Add question for {} points".
                                        format(self.point_counter)
                                        ).grid(row = self.question_counter+1, column =0)
            self.question_entry = Entry(self).grid(row = self.question_counter+1, column = 1, ipadx = 100)
            self.add_button = Button(self, text = "Add question",
                                     command = db.DBWriter().save_question
                                     ).grid(row = self.question_counter + 1, column = 2)

            return None

        self.question_buttons = []
        self.question_counter = 0
        self.point_counter = 0
        self.table_name_label = Label(self, text = "Add your game name:").grid(row = 0, column = 0)
        self.table_name_entry = Entry(self).grid(row = 0, column = 1)
        self.add_question_button = Button(self, text = "Add question", command = add_question_row)\
            .grid(row = 1, column = 0)



        # self.edit_questions = Button(self, command = self.initialize_questions,
        #                              text="Edit questions").grid(row=2, column=0)
        # self.quit = Button(self, command=self.quit_game,
        #                    text="Quit").grid(row=3,column=0)
        # """Welcome label"""
        # text = "Welcome to flipquiz, game made to enhance people language skills. Feel free to use it! "
        # """Welcome label"""
        # self.welcome_label = Label(self, text=text).grid(row=0, column=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Add new table")
        self.pack()
        self.create_widgets()
        self.mainloop()

if __name__ == "__main__":
    TableToolkitFrontend()