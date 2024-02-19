from Posts import Posts


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
            print("Follow succeeded")

    def unfollow(self, user):
        if self.isConnected:
            self.followers.remove(user)
            user.followers.remove(Users(self.name, self.password))
            print("Unfollow succeeded")

    def publish_post(self, type_post, *content):  # using factory
        if self.isConnected:
            post = Posts.create_post(type_post, Users(self.name, self.password), *content)
            return post

    def notify(self, new_post):
        print("Received a notification for a new post")
        for follower in self.followers:
            follower.notification(new_post)

    @staticmethod
    def print_info(self, user):
        print(f"Followers: {user.followers}")
        print(f"Posts: {user.posts}")
        print(f"Notification: {user.notification}")


    def print_notifications(self):
        for notif in reversed(self.notification):
            print(notif)
