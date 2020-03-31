from tkinter import *
from src.db_handler import DBWriter
from src import question_classer as qc
from functools import partial


class EditScreen(Frame):

    def initialize_gui(self):
        games = StringVar(self)
        select_label = Label(self, text = "Select game").grid(row = 0, column = 0)
        menu = OptionMenu(self, games, *DBWriter("DB/questions.db").get_games())
        menu.config(fg="red",bg='deep sky blue')
        menu.grid(row=1, column=0)
        load_button = Button(self, text = "Load",
                             command = lambda : [initialize_question_table(DBWriter('DB/questions.db').
                                                                           load_data(games.get()))]).grid(row = 1, column = 1)

        def initialize_question_table(game):
            print(game)
            labels_id = []
            labels_question = []
            labels_category = []
            labels_points = []
            buttons_edit = []
            main_label_id = Label(self, text = "id").grid(column = 0, row = 2)
            main_label_question = Label(self, text = "Question").grid(column = 1, row = 2)
            main_label_category = Label(self, text = "Category").grid(column = 2, row = 2)
            main_label_points = Label(self, text = "Points").grid(column = 3, row = 2)

            def edit_question(dataframe):
                question_id = dataframe['question_id'].values
                points = dataframe['Points'].values
                edit_window = Tk()
                edit_window.wm_title("Question number {}".format(question_id))
                id_label = Label(edit_window, text = question_id).grid(row =0, column = 0)
                question_edit = Entry(edit_window)
                question_edit.grid(row=0, column=1, ipadx=100)
                category_entry = Entry(edit_window)
                category_entry.grid(row=0, column=2, ipadx=30)
                point_label = Label(edit_window, text = points).grid(row = 0, column = 3)


                def correct_data():
                    return qc.MakeQuestions(question_id=question_id,
                                            category=category_entry.get(),
                                            points=points,
                                            question= question_edit.get(),
                                            game=game).row()

                save_exit_button = Button(edit_window, text = "Save & Exit", command = correct_data).grid(row=0,column=4)







            for i in range(len(game['question_id'])):
                question_loc = game.loc[game['question_id'] == i]

                labels_id.append(Label(self, text= question_loc['question_id'].values[0],
                                     height = 1,
                                     width = 1))
                labels_id[i].grid(column=0, row=i+3)
                labels_question.append(Label(self, text= question_loc['Question'].values[0],
                                     height = 3,
                                     width = 40))
                labels_question[i].grid(column=1, row=i+3)
                labels_category.append(Label(self, text= question_loc['Category'].values[0],
                                     height = 3,
                                     width = 12))
                labels_category[i].grid(column=2, row=i+3)
                labels_points.append(Label(self, text= question_loc['Points'].values[0],
                                     height = 3,
                                     width = 12))
                labels_points[i].grid(column=3, row=i+3)
                buttons_edit.append(Button(self, text = "Edit",
                                           command = partial(edit_question, question_loc)))
                                                              #print(game.loc[game['question_id'] == i])]))
                buttons_edit[i].grid(column=4, row = i+3)




    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Edit data")
        self.pack()
        self.initialize_gui()
        self.mainloop()

if __name__ == "__main__":
    EditScreen().initialize_gui()