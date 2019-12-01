import os
import pandas as pd
from src.DB import *

file = 'DB/database.txt'


class QuestionReader:

    def __init__(self):
        pass

    def read_question(self, file):
        data = pd.read_csv(file, sep = ',', header = None)
        print(data.head())

QuestionReader().read_question(file)