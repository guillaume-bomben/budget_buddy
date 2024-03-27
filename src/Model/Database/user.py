from DB import DB

class User(DB):
    def __init__(self):
        super().__init__()
        self.data_list = []
        self.read()
        
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