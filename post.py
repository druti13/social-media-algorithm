# post.py

from datetime import datetime

class Post:
    def __init__(self, user, content, timestamp=None, media=None, hashtags=None, geotag=None):
        self.user = user
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.media = media or []
        self.hashtags = hashtags or []
        self.geotag = geotag
        self.likes = 0
        self.comments = []
        self.shares = 0
        self.reactions = {"like": 0, "love": 0, "wow": 0, "sad": 0, "angry": 0}

    def __repr__(self):
        return f"Post(user={self.user.username}, content='{self.content[:20]}...', timestamp={self.timestamp})"
