from tkinter import *
from src.prepare_questions import QuestionReader



class Front(Frame):

        def get_question(self, id):
            question_window = Tk()
            question_window.wm_title("Question number {}".format(id+1))
            question = QuestionReader(id).read_question()

            def exit():
                question_window.destroy()

            label_question = Label(question_window, text = question, height = 6, width = 65, font = ("Arial", 25), bg = "lightblue")
            label_time = Label(question_window, text = '', width = 10)
            label_question.grid(row = 0, column = 0)
            label_time.grid(row = 1, column = 0)
            button_exit = Button(question_window, text = "Exit", command = exit)
            button_exit.grid(row = 2, column = 0)

            def countdown(count):
                label_time['text'] = count

                if count > 0:
                    question_window.after(1000, countdown, count - 1)
            countdown(60)

            question_window.mainloop()

        def create_widgets(self):
            button = []
            label_names = ['Vocabulary - 1', 'Vocabulary - 2', 'Grammar - modals', 'Grammar - passive', 'Misc', 'Fun!']
            labels = []
            counter = 0
            columns = 0
            for i in range(30):
                button.append(Button(self, text=str((counter+ 1) * 100),
                                     height = 7,
                                     width = 24,
                                     command = lambda index=i: [disable(index), self.get_question(index)],
                                     fg = "yellow",
                                     bg = "green"))
                button[i].grid(column=columns, row=counter+1, sticky=W)
                counter += 1
                if counter % 5 == 0:
                    labels.append(Label(self, text=label_names[columns], height = 3, width = 24))
                    labels[columns].grid(column=columns, row = 0)
                    counter = 0
                    columns += 1

            def disable(i):

                button[i].config(state="disabled", bg="blue")

        def __init__(self, master = None):
            Frame.__init__(self, master)
            self.winfo_toplevel().title("Flip the buttons!")
            self.pack()
            self.create_widgets()
            self.mainloop()


