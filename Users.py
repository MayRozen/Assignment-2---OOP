from Posts import Posts
from SocialNetwork import SocialNetwork


class Users:
    followers = []
    posts = []
    notification = []
    isConnected = False
    name = None
    password = None

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.isConnected = False

    def follow(self, user):
        if self.isConnected:
            self.followers.append(user)
            user.followers.append(Users(self.name, self.password))

    def unfollow(self, user):
        if self.isConnected:
            self.followers.remove(user)
            user.followers.remove(Users(self.name, self.password))

    def publish_post(self, type_post, *content):  # using factory
        post = Posts.create_post(type_post, Users(self.name, self.password), *content)
        return post

    def notify(self):
        pass

    def print_info(self):
        pass

    def print_notifications(self):
        pass
