import os, sqlite3

class DBWriter:

    def save_question(self):
        print("satan")

    def exportToDB(dataframe, tbl_name, db_name):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        wildcards = ','.join(['?'] * len(dataframe.columns))
        data = [tuple(x) for x in dataframe.values]

        col_str = '"' + '","'.join(dataframe.columns) + '"'
        cur.execute("create table IF NOT EXISTS %s (%s)" % (tbl_name, col_str))
        cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)

        conn.commit()
        conn.close()

    # Database creation
    def saveEntry(self, newEntry):
        date = newEntry.date
        login = newEntry.login
        url = newEntry.url
        password = newEntry.password
        dfList = [date,
                  login,
                  url,
                  password]
        dataframe = pd.DataFrame(dfList)
        dataframe = dataframe.transpose()
        dataframe.columns = ['Date', 'Login', 'Url', 'Password']
        DBWriter.exportToDB(dataframe, 'passwords', 'testDB.db')