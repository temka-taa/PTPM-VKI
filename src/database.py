import sqlite3


class w_DB:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT, a_passw TEXT, result TEXT, message TEXT)")
    def add(self, login, password, a_passw, res_bool, res_msg):
        self.conn.execute("INSERT INTO users (login, password, a_passw, result, message) VALUES (?,?,?,?,?)", (login, password, a_passw, res_bool, res_msg))
        self.conn.commit()
    def get(self, login, password, a_passw):
        row = self.conn.execute("select * from users where login = ? and password = ? and a_passw = ?", (login, password, a_passw)).fetchone()
        return row
    def delete(self, login, password, a_passw):
        self.conn.execute("delete from users where login = ? and password = ? and a_passw = ?", (login, password, a_passw))
        self.conn.commit()