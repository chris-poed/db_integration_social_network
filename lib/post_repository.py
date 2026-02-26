from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(item)
        return posts
    
    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE user_id = %s', [user_id])
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(item)
        return posts
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)', [post.title, post.content, post.views, post.user_id])
        return None