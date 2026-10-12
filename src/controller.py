class Controller:
    def __init__(self, valid, hand, db, sender):
        self.validator = valid
        self.inp = hand
        self.db = db
        self.sender = sender
    def run(self):
        data = self.inp.get_data()
        login, password, a_pass = data
        result, msg = self.validator.valid(login, password, a_pass)
        self.sender.send(f"Пользователь {login}, {msg}")
        return result,msg