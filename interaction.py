

import random

def like_post(post):
    post.likes += 1

def comment_post(post, comment):
    post.comments.append(comment)

def share_post(post):
    post.shares += 1

def react_post(post, reaction):
    if reaction in post.reactions:
        post.reactions[reaction] += 1

def simulate_interactions(posts):
    for post in posts:
        post.likes = random.randint(0, 100)
        post.shares = random.randint(0, 10)
        post.comments = [f"Comment {i}" for i in range(random.randint(0, 20))]
        post.reactions = {
            "like": random.randint(0, 50),
            "love": random.randint(0, 20),
            "wow": random.randint(0, 10),
            "sad": random.randint(0, 5),
            "angry": random.randint(0, 5)
        }
