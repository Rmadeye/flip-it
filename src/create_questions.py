from tkinter import *
from src import add_table_toolkit

class QuestionsFrontend(Frame):

    def create_widgets(self):

        def quit_window():
            Frame.destroy(self)


        self.add_table = Button(self, text = "Add table",
                                command = add_table_toolkit.TableToolkitFrontend).grid(row=0,column=0)
        self.edit_table = Button(self, text="Edit table").grid(row=1, column=0)
        self.quit = Button(self, command=quit_window,
                           text="Quit").grid(row=2,column=0)



    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Create questions")
        self.pack()
        self.create_widgets()
        self.mainloop()





if __name__ == "__main__":

    QuestionsFrontend()