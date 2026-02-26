from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['email_address'], row['username'])
            users.append(item)
        return users
    
    def find(self, user_id):
        row = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])[0]
        return User(row['id'], row['email_address'], row['username'])
        