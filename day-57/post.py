import requests


class Post:
    no_post = {
        "id": 0,
        "title": "UNKNOWN",
        "subtitle": "No Post for ID",
        "body": "There is no post"
    }

    def __init__(self):
        response = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        print(f"DEBUG: {response.json()}")
        self.posts = response.json()

    def get_posts(self):
        return self.posts

    def get_post(self, post_id):
        print(f"DEBUG: post_id = {post_id}")
        matched_post = self.no_post
        for post in self.posts:
            print(f"DEBUG: post = {post}")
            print(f"DEBUG: check = {post['id'] == post_id}")
            print(f"DEBUG: post_id = {post_id} with post = {post['id']}")
            if int(post['id']) == int(post_id):
                matched_post = post
        return matched_post
