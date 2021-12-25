import mysql.connector

class Database:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            user='root',
            host='localhost',
            password='124Jackshit@',
            port=3306,
            database='onlinemovie')
        self.my_cursor = self.my_connection.cursor()

    def normalexecvalues(self,query,values):
        self.my_cursor.execute(query,values)
        self.my_connection.commit()

    def get_all_data(self,query):
        self.my_cursor.execute(query)
        data = self.my_cursor.fetchall()
        return data

    def fetch_data(self,query,values):
        self.my_cursor.execute(query,values)
        data = self.my_cursor.fetchall()
        return data

    def normalexec(self,query):
        self.my_cursor.execute(query)
        self.my_connection.commit()











