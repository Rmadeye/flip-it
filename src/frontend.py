from tkinter import *
from src.prepare_questions import QuestionReader



class Front:


    def __init__(self):
        window = Tk()
        window.wm_title("Flip the buttons!")

        """ GUI """

        def disable(i):

            button[i].config(state = "disabled", bg = "blue")

        def get_question(id):
            QuestionReader().read_question('database.txt')



        button = []
        label_names = ['Vocabulary', 'Grammar', 'Speaking', 'Pronoun.', 'Misc']
        labels = []
        counter = 0
        columns = 0
        for i in range(25):
            button.append(Button(window, text=str((counter+ 1) * 100), height = 6, width = 20, command = lambda index=i: [disable(index), print("chuj")], fg = "yellow", bg = "green"))
            button[i].grid(column=columns, row=counter+1, sticky=W)
            counter += 1
            if counter % 5 == 0:
                labels.append(Label(window, text=label_names[columns], height = 6, width = 20))
                labels[columns].grid(column=columns, row = 0)
                counter = 0
                columns += 1

        window.mainloop()


if __name__ == "__main__":
    Front()