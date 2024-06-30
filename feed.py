# feed.py
import random
from datetime import datetime, timedelta
from post import Post


def generate_sample_posts(users):
    posts = []
    content = [
        "Hello world!",
        "Amazing sunset photo!",
        "Loving the weather today!",
        "New recipe idea: Pasta Carbonara",
        "Throwback to last summer's vacation 🌴"
    ]
    for user in users:
        for _ in range(random.randint(1, 3)):
            post_content = random.choice(content)
            post_timestamp = datetime.now() - timedelta(days=random.randint(0, 7))
            posts.append(Post(user, post_content, post_timestamp))
    return posts

def post_score(post, user):
    # Advanced scoring algorithm considering user interests, recency, and engagement
    interest_score = len(set(post.hashtags) & set(user.interests))
    engagement_score = post.likes + post.shares + sum(post.reactions.values())
    recency_score = (datetime.now() - post.timestamp).days
    return (interest_score * 2 + engagement_score) / (recency_score + 1)

def sort_feed(posts, user):
    user_interests = set(user.interests)
    personalized_posts = [post for post in posts if any(tag in user_interests for tag in post.hashtags)]

    sorted_posts = sorted(personalized_posts, key=lambda post: post_score(post, user), reverse=True)
    return sorted_posts

def trending_hashtags(posts):
    hashtag_counts = {}
    for post in posts:
        for tag in post.hashtags:
            if tag in hashtag_counts:
                hashtag_counts[tag] += 1
            else:
                hashtag_counts[tag] = 1
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    return [tag for tag, count in sorted_hashtags[:5]]
