from src import db_handler

class MakeQuestions:

    def __init__(self, question, points, id):
        self.question = question
        self.points = points
        self.id = id

    def row(self):
        entry = (self.question, self.points, self.id)
        return db_handler

