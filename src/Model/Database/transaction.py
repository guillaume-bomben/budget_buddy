from src.Model.Database.DB import DB

class transaction(DB):
    def __init__(self):
        super().__init__()
        self.data_list = []
        self.read()

    def create(self,id_user_send,id_user_recive,description,amount,type):
        query = "INSERT INTO transaction (id_user_send,id_user_recive,description,amount,type) VALUES (%s,%s,%s,%s,%s)"
        param = (id_user_send,id_user_recive,description,amount,type)
        self.executeQuery(query,param)

    def read(self):
        query = "SELECT * FROM transaction"
        self.data_list = []
        for line in self.fetch(query):
            self.data_list.append(line)

    def delete(self,id):
        query = "DELETE FROM transaction WHERE id = %s"
        param = (id,)
        self.executeQuery(query,param)

    def get_transaction(self,id):
        query = "SELECT * FROM transaction WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)

    def get_id(self,id_user_send,id_user_recive,description,amount,type):
        query = "SELECT id FROM transaction WHERE id_user_send = %s AND id_user_recive = %s AND description = %s AND amount = %s AND type = %s"
        param = (id_user_send,id_user_recive,description,amount,type)
        return self.fetch(query,param)[0]['id']

    def get_id_user_send(self,id):
        query = "SELECT id_user_send FROM transaction WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)

    def get_id_user_recive(self,id):
        query = "SELECT id_user_recive FROM transaction WHERE id = %s"
        param = (id,)
        return self.fetch(query,param)