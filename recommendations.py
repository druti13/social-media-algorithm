# recommendations.py

def suggest_friends(user, users):
    potential_friends = [u for u in users if u != user and len(u.followers - user.following) > 5]
    return potential_friends[:5]

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
