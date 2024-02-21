

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
        self.isConnected = True

    def follow(self, user):
        if self.isConnected:
            user.followers.append(self)
            print("Follow succeeded")

    def unfollow(self, user):
        if self.isConnected:
            user.followers.remove(self)
            print("Unfollow succeeded")

    def publish_post(self, type_post, *content):  # using factory
        if self.isConnected:
            post = Posts.create_post(type_post, Users(self.name, self.password), *content)
            return post

    @staticmethod
    def print_info(self, user):
        print(f"Followers: {user.followers}")
        print(f"Posts: {user.posts}")
        print(f"Notification: {user.notification}")

    def print_notifications(self):
        for notif in reversed(self.notification):
            print(notif)

    def updateLike(self, like_count):
        print(f"{self.name} liked your post: {like_count}")
        self.notification.append(like_count)

    def updateComment(self, content):
        print(f"{self.name} commented on th post: {content}")
        self.notification.append(content)

    def updatePost(self, new_post):
        print(f"{self.name} received newsletter: {new_post}")
        self.notification.append(new_post)

