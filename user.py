

class User:
    def __init__(self, username, interests=None):
        self.username = username
        self.interests = interests or []
        self.following = set()
        self.followers = set()
        self.feed = []

    def follow(self, user):
        self.following.add(user)
        user.followers.add(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

    def __repr__(self):
        return f"User(username={self.username}, interests={self.interests})"
