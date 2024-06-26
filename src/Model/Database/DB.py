import mysql.connector

class DB:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '1234'
        self.database = 'Budget_Buddy'

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def executeQuery(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        self.connection.commit()
        self.disconnect()

    def fetch(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    