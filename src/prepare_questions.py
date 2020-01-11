import pandas as pd




class QuestionReader:

    def __init__(self, id):
        self.file = r'src/DB/database.txt'
        self.id = id

    def read_question(self):
        data = pd.read_csv(self.file, sep = ',')
        question = data['quest'].values[self.id]
        return question
