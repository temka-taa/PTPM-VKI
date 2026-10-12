class Controller:
    def __init__(self, valid, hand, db, sender):
        self.validator = valid
        self.inp = hand
        self.db = db
        self.sender = sender
    def run(self):
        data = self.inp.get_data()
        login, password, a_passw = data
        row = self.db.get(login, password, a_passw)
        if row is None:
            result, msg = self.validator.valid(login, password, a_passw)
            self.db.add(login, password, a_passw, result, msg )
        else:
            result, msg = row[3], row[4]
        self.sender.send(f"Пользователь {login}, {msg}")
        return result, msg
