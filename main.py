# main.py

from user import User
from post import Post
from interaction import simulate_interactions, like_post, comment_post, share_post, react_post
from feed import generate_sample_posts, sort_feed, trending_hashtags
from activity_log import log_activity

def get_user_input():
    num_users = int(input("Enter the number of users: "))
    users = []
    for _ in range(num_users):
        username = input("Enter username: ")
        interests = input("Enter interests (comma-separated): ").split(",")
        users.append(User(username, interests=[interest.strip() for interest in interests]))
    return users

def main():
    # Get user input for creating users
    users = get_user_input()

    # Generate sample posts
    posts = generate_sample_posts(users)

    # Simulate interactions (likes, comments, shares, reactions)
    simulate_interactions(posts)

    # Generate feed for each user
    for user in users:
        user_feed = sort_feed(posts, user)
        print(f"\n--- Feed for {user.username} ---")
        for post in user_feed:
            print(f"User: {post.user.username} | Content: {post.content} | Likes: {post.likes} | Comments: {len(post.comments)} | Shares: {post.shares} | Reactions: {post.reactions}")

    # Example trending hashtags
    trending_tags = trending_hashtags(posts)
    print("\n--- Trending Hashtags ---")
    for tag in trending_tags:
        print(tag)

    # Generate and display friend suggestions for each user
    for user in users:
        friend_suggestions = suggest_friends(user, users)
        print(f"\n--- Friend Suggestions for {user.username} ---")
        for friend in friend_suggestions:
            print(friend.username)

if __name__ == "__main__":
    main()
