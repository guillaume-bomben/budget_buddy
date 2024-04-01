from src.Model.Database.DB import DB

class User(DB):
    def __init__(self):
        super().__init__()
        self.data_list = []
        self.user_list = []
        self.read()
        self.get_user_list()
        
    def create(self,lastname,firstname,email,password,balance):
        query = "INSERT INTO user (last_name,first_name,email,password,balance) VALUES (%s,%s,%s,%s,%s)"
        param = (lastname,firstname,email,password,balance)
        self.executeQuery(query,param)
    
    def read(self):
        query = "SELECT * FROM user"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)

    def delete(self,id):
        query = "DELETE FROM user WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)

    def get_balance(self,id):
        query = "SELECT balance FROM user WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)[0]['balance']

    def update_balance(self,id,balance):
        query = "UPDATE user SET balance = %s WHERE id = %s"
        param = (balance,id)
        self.executeQuery(query,param)

    def get_id(self,email,password):
        query = "SELECT id FROM user WHERE email = %s AND password = %s"
        param = (email,password)
        return self.fetch(query,param)

    def get_user(self,id):
        query = "SELECT * FROM user WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)
    
    def verify_email(self,email):
        query = "SELECT id FROM user WHERE email = %s"
        param = (email,)
        return self.fetch(query,param)
    
    def get_user_list(self):
        query = "SELECT id,first_name,last_name FROM user"
        self.user_list = []
        for line in self.fetch(query):
            self.user_list.append(line)
        return self.user_list