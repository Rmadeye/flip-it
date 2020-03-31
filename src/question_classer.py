from src import db_handler
import pandas as pd

class MakeQuestions:

    def __init__(self, question, category, points, question_id, game):
        self.question = question
        self.points = points
        self.question_id = question_id
        self.game = game
        self.category = category

    def row(self):
        entry = [self.question_id, self.question, self.category, self.points]
        dataframe = pd.DataFrame(entry)
        dataframe = dataframe.transpose()
        dataframe.columns = ['question_id', 'Question', 'Category', 'Points']
        print(dataframe)
        return db_handler.DBWriter('src/DB/questions.db').exportToDB(dataframe, self.game)
