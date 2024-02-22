from enum import Enum
from abc import abstractmethod

from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

from Observer import Sender

class PostType(Enum):
    TEXTPOST = "textPost"
    IMAGEPOST = "imagePost"
    SALEPOST = "salePost"


class Posts:
    _like = []
    comments = []

    def __init__(self, user):
        self._user = user
        self.sender = Sender()

    @staticmethod
    def publish_post(self, post_type, *content):
        if self.isConnected:
            if post_type == post_type.TEXTPOST:
                new_post = TextPost(self, *content)
                self._posts.append(new_post)
                self.sender.notify(f"{self._username} has a new post")
                return new_post
            elif post_type == post_type.IMAGEPOST:
                new_post = ImagePost(self, *content)
                self._posts.append(new_post)
                self.sender.notify(f"{self._username} has a new post")
                return new_post
            elif post_type == post_type.SALEPOST:
                description = content[0]
                price = content[1]
                location = content[2]
                new_post = SalePost(description, price, location, self)
                self._posts.append(new_post)
                self.sender.notify(f"{self._username} has a new post")
                return new_post
            else:
                raise ValueError("Invalid post type")



    def like(self, user):
        if self._user.isConnected:
            if user != self._user and user not in self._like:
                self._user.notifications.append(f"{user.username()} liked your post")
                print(f"notification to {self._user.username()}: {user.username()} liked your post")

    def comment(self, user, content):
        if self._user.isConnected:
            if user != self._user:
                self._user.notifications.append(f"{user.username()} commented on your post")
                print(f"notification to {self._user.username()}: {user.username()} commented on your post: {content}")

    @abstractmethod
    def print_info(self, user):
        pass

