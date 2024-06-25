import requests


class Post:
    no_post = {
        "id": 0,
        "title": "UNKNOWN",
        "subtitle": "No Post for ID",
        "body": "There is no post",
        "author": "NOBODY",
        "dates": "00-00-00",
        "image_url": "https://cdn-icons-png.flaticon.com/512/6478/6478111.png"
    }

    def __init__(self):
        response = requests.get(f"https://api.npoint.io/787c8b4eb68b8b3189e0")
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
