from enum import Enum
from abc import abstractmethod

import Users

class PostType(Enum):
    TEXTPOST = "textPost"
    IMAGEPOST = "imagePost"
    SALEPOST = "salePost"


class Posts:
    like_count = 0
    comments = []
    owner = None

    @staticmethod
    def create_post(self, post_type, owner, *content):
        self.owner = owner
        if post_type == post_type.TEXTPOST:
            text = content[0]
            return TextPost(text)
        elif post_type == post_type.IMAGEPOST:
            image = content[0]
            return ImagePost(image)
        elif post_type == post_type.SALEPOST:
            description = content[0]
            price = content[1]
            location = content[2]
            return SalePost(description, price, location)
        else:
            raise ValueError("Invalid post type")

    def like(self, user):  # continue
        if self.owner.isConnected:
            self.like_count += 1
            if user != self.owner:
                for follower in self.owner.followers:
                    self.owner.followers.updateLike(self.like_count)

    def comment(self, user, content):
        if self.owner.isConnected:
            self.comments.append(user, content)
            if user != self.owner:
                for follower in self.owner.followers:
                    self.owner.followers.updateComment(content)

    @abstractmethod
    def print_info(self, user):
        pass


    def notify(self, new_post):
        for follower in self.owner.followers:
            Users.followers.updatePost(new_post)

