class User:
    def __init__(self, _id, _username):
        self.id = _id
        self.username = _username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def __str__(self):
        return (f"ID: {self.id}, Username: {self.username} "
                f"is following  {self.following} users and has {self.followers} followers.")


user_1 = User("001", "James")
user_2 = User("002", "Fred")

user_1.follow(user_2)

print(user_1)
print(user_2)
