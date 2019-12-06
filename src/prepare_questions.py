import pandas as pd
from src.DB import *




class QuestionReader:

    def __init__(self):
        pass

    def read_question(self, id):
        file = r'src/DB/database.txt'
        data = pd.read_csv(file, sep = ',')
        question = data['quest'].values[id]
        return question
