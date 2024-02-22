from Observer import Sender

class Users:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._followers = []
        self._posts = []
        self.notification = []
        self.isConnected = False
        self.sender = Sender()

    def username(self):  # get username
        return self._username

    def password(self):  # get password
        return self._password

    def follow(self, user):
        if self.isConnected:
            if self not in user._followers:
                user._followers.append(self)
                user.sender.register(self)  # Observer
                print(f"{self._username} started following {user._username}")

    def unfollow(self, user):
        if self.isConnected:
            if self not in user._followers:
                user._followers.remove(self)
                user.sender.unregister(self)  # Observer
                print(f"{self._username} unfollowed {user._username}")

    def publish_post(self, type_post, *content):  # using factory
        if self.isConnected:
            post = Posts.publish_post(type_post, Users(self._username, self._password), *content)
            return post

    def print_info(self):
        print(f"User name: {self._username}")
        print(f"Number of followers: {len(self._followers)}")
        print(f"Number of posts: {len(self._posts)}")

    def print_notifications(self):
        for notif in reversed(self.notification):
            print(notif)

    def update(self, content):
        self.notification.append(content)


