import os, sqlite3, pandas
class DBWriter:

    def __init__(self, db_name):
        self.db_name = db_name


    def exportToDB(self, dataframe, tbl_name):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()

        wildcards = ','.join(['?'] * len(dataframe.columns))
        data = [tuple(x) for x in dataframe.values]

        col_str = '"' + '","'.join(dataframe.columns) + '"'
        cur.execute("create table IF NOT EXISTS %s (%s)" % (tbl_name, col_str))
        question_id = int(dataframe['question_id'].values)
        cur.execute("SELECT question_id FROM {} WHERE question_id=(?)".format(tbl_name), (question_id,))
        result = cur.fetchall()
        # cur.execute('SELECT COUNT(Name) FROM "{}" WHERE Name=?'.format(group.replace('"', '""')), (food,))
        if result:
            print("I see")
            cur.execute("DELETE FROM {} WHERE question_id=(?)".format(tbl_name), (question_id,))
            cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
            conn.commit()
            conn.close()

        else:
            print("I dont:", result)
            cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)
            conn.commit()
            conn.close()

    def get_games(self):
        conn = sqlite3.connect(self.db_name)
        games = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # print(game for game in games)
        return [game[0] for game in games]

    def load_data(self, game):
        conn = sqlite3.connect(self.db_name)

        return pandas.read_sql_query("SELECT * FROM {}".format(game),conn)



if __name__ == "__main__":
    DBWriter('DB/questions.db').load_data('a')

