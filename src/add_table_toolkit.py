from tkinter import *
from src import question_classer as qc

class TableToolkitFrontend(Frame):

    def create_widgets(self):
        def add_question_row():
            self.question_counter += 1
            self.point_counter += 100
            if self.point_counter > 500:
                self.point_counter = 100
            self.question_label = Label(self, text = "Question for {} points".
                                        format(self.point_counter)
                                        ).grid(row = self.question_counter+1, column =0)
            self.question_entry = Entry(self)
            self.question_entry.grid(row = self.question_counter+1, column = 1, ipadx = 100)
            self.category_entry = Entry(self)
            self.category_entry.grid(row = self.question_counter+1, column = 2, ipadx = 30)


            def get_data():
                return qc.MakeQuestions(question_id = self.question_counter - 1,
                                        category = self.category_entry.get(),
                                                                points = self.point_counter,
                                                                question = self.question_entry.get(),
                                                                game = self.table_name_entry.get()).row()

            self.add_button = Button(self, text = "Add to database",
                                     command = get_data
                                     ).grid(row = self.question_counter + 1, column = 3)

            return None

        self.question_buttons = []
        self.question_counter = 0
        self.point_counter = 0
        self.table_name_label = Label(self, text = "Add your game name:").grid(row = 0, column = 0)
        self.table_name_entry = Entry(self)
        self.table_name_entry.grid(row = 0, column = 1)
        self.add_question_button = Button(self, text = "Add question", command = add_question_row)\
            .grid(row = 1, column = 0)
        self.category_label = Label(self, text='Category').grid(row=1, column=2)
        self.question = Label(self, text='Question').grid(row=1, column=1)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Add new table")
        self.pack()
        self.create_widgets()
        self.mainloop()

if __name__ == "__main__":
    TableToolkitFrontend()