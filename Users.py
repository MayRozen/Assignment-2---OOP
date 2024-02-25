from Observer import Sender
from FactoryPosts import FactoryPosts, PostType


class Users:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self.followers = []
        self._posts = []
        self.notification = []
        self.isConnected = True
        self.sender = Sender()

    def username(self):  # get username
        return self._username

    def password(self):  # get password
        return self._password

    def follow(self, user):
        if self.isConnected:
            if self not in user.followers:
                user.followers.append(self)
                user.sender.register(self)  # Observer
                print(f"{self._username} started following {user.username()}")

    def unfollow(self, user):
        if self.isConnected:
            if self in user.followers:
                user.followers.remove(self)
                user.sender.unregister(self)  # Observer
                print(f"{self._username} unfollowed {user.username()}")

    def publish_post(self, type_post, *content):  # using factory
        if self.isConnected:
            if(type_post == "Text"):
                new_post = FactoryPosts.created_post(PostType.TEXTPOST, self, *content)
                self._posts.append(new_post)
            if(type_post == "Image"):
                new_post = FactoryPosts.created_post(PostType.IMAGEPOST, self, *content)
                self._posts.append(new_post)
            if (type_post == "Sale"):
                new_post = FactoryPosts.created_post(PostType.SALEPOST, self, *content)
                self._posts.append(new_post)

            self.sender.notify(f"{self._username} has a new post")
            print(str(self._posts[-1]))
            return self._posts[-1]

    def __str__(self):
        a = f"User name: {self._username}, "
        b = f"Number of posts: {len(self._posts)}, "
        c = f"Number of followers: {len(self.followers)}"

        return a+b+c

    def print_notifications(self):
        print(f"{self._username}'s notifications:")
        for notif in self.notification:
            print(notif)

    def update(self, content):
        self.notification.append(content)
