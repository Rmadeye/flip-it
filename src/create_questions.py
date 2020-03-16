from tkinter import *

class QuestionsFrontend(Frame):

    def create_widgets(self):
        self.add_table = Button(self, text = "Add table").grid(row=0,column=0)
        self.edit_table = Button(self, text="Edit table").grid(row=1, column=0)
        self.quit = Button(self, command=self.quit_window,
                           text="Quit").grid(row=2,column=0)

    def quit_window(self):
        return Frame.destroy(self)

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Create questions")
        self.pack()
        self.create_widgets()
        self.mainloop()





if __name__ == "__main__":

    QuestionsFrontend()