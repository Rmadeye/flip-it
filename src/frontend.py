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

           question = QuestionReader().read_question(id)
           question_window = Tk()
           question_window.wm_title("Question number {}".format(id))
           label_question = Label(question_window, text = question, height = 6, width = 55, font = ("Arial", 25), bg = "lightblue")
           label_time = Label(question_window, text = '', width = 10)
           label_question.grid(row = 0, column = 0)
           label_time.grid(row = 1, column = 0)

           def countdown(count):
               # change text in label
               label_time['text'] = count

               if count > 0:
                   question_window.after(1000, countdown, count - 1)

           countdown(60)


           question_window.mainloop()

        background_image = PhotoImage("src/DB/brain_lt.png")
        background_label = Label(window, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        button = []
        label_names = ['Vocabulary - 1', 'Vocabulary - 2', 'Grammar - 1', 'Grammar - 2', 'Misc', 'Fun!']
        labels = []
        counter = 0
        columns = 0
        for i in range(25):
            button.append(Button(window, text=str((counter+ 1) * 100),
                                 height = 7,
                                 width = 24,
                                 command = lambda index=i: [disable(index), get_question(index)],
                                 fg = "yellow",
                                 bg = "green"))
            button[i].grid(column=columns, row=counter+1, sticky=W)
            counter += 1
            if counter % 5 == 0:
                labels.append(Label(window, text=label_names[columns], height = 3, width = 24))
                labels[columns].grid(column=columns, row = 0)
                counter = 0
                columns += 1

        window.mainloop()


if __name__ == "__main__":
    Front()