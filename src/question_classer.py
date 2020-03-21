from src import db_handler
import pandas as pd

class MakeQuestions:

    def __init__(self, question, category, points, id, game):
        self.question = question
        self.points = points
        self.id = id
        self.game = game
        self.category = category

    def row(self):
        entry = [self.id, self.question, self.category, self.points]
        dataframe = pd.DataFrame(entry)
        dataframe = dataframe.transpose()
        dataframe.columns = ['id', 'Question', 'Category', 'Points']
        return db_handler.DBWriter('DB/questions.db').exportToDB(dataframe, self.game)
