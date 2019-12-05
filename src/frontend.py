from tkinter import *
from src.prepare_questions import QuestionReader



class Front:


    def __init__(self):
        window = Tk()
        window.wm_title("Flip the buttons!")

        """ GUI """

        def disable(i):

            button[i].config(state = "disabled", bg = "blue")

        def get_question(id, remaining = 60):

           question = QuestionReader().read_question(id)
           question_window = Tk()
           label_question = Label(question_window, text = question, height = 6, width = 20, font = ("Arial", 25), bg = "lightblue")
           label_time = Label(question_window, text = '', width = 10)
           label_question.grid(row = 0, column = 0)

           if remaining <= 0:
               label_time.configure(text="time's up!")
           else:
               label_time.configure(text="%d" % remaining)
               remaining = remaining - 1


           question_window.mainloop()





        button = []
        label_names = ['Vocabulary', 'Grammar', 'Speaking', 'Pronoun.', 'Misc']
        labels = []
        counter = 0
        columns = 0
        for i in range(25):
            button.append(Button(window, text=str((counter+ 1) * 100),
                                 height = 6,
                                 width = 20,
                                 command = lambda index=i: [disable(index), get_question(index)],
                                 fg = "yellow",
                                 bg = "green"))
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