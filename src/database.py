import sqlite3


class DatabaseRepository:
    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL CHECK (length(name) <= 256),
                message TEXT NOT NULL CHECK (length(message) <= 8096)
            )
        ''')
        self.conn.commit()

    def get_by_id(self, comment_id):
        row = self.conn.execute(
            'SELECT * FROM comments WHERE id = ?',
            (comment_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_by_name(self, username):
        rows = self.conn.execute(
            'SELECT * FROM comments WHERE name = ?',
            (username,)
        ).fetchall()
        return [dict(row) for row in rows]

    def add(self, comment_id, username, message):
        self.conn.execute(
            'INSERT INTO comments (id, name, message) VALUES (?, ?, ?)',
            (comment_id, username, message),
        )
        self.conn.commit()
        return True

    def update(self, comment_id, new_message):
        cur = self.conn.execute(
            'UPDATE comments SET message = ? WHERE id = ?',
            (new_message, comment_id),
        )
        self.conn.commit()
        return cur.rowcount > 0

    def delete(self, comment_id):
        cur = self.conn.execute(
            'DELETE FROM comments WHERE id = ?', (comment_id,)
        )
        self.conn.commit()
        return cur.rowcount > 0

    def close(self):
        self.conn.close()