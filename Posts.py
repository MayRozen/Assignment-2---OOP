from enum import Enum
from abc import ABC, abstractmethod

from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost
from Users import Users


class PostType(Enum):
    TEXTPOST = "textPost"
    IMAGEPOST = "imagePost"
    SALEPOST = "salePost"


class Posts:
    like_count = 0
    comments = []
    owner = None

    def create_post(self, post_type, owner, *content):  # Factory
        if owner.isConnected:
            if post_type == post_type.TEXTPOST:
                text = content[0]
                print("Text Post")
                return TextPost(text)
            elif post_type == post_type.IMAGEPOST:
                image = content[0]
                print("Image Post")
                return ImagePost(image)
            elif post_type == post_type.SALEPOST:
                description = content[0]
                price = content[1]
                location = content[2]
                print("Sale Post")
                return SalePost(description, price, location)
            else:
                raise ValueError("Invalid post type")

    def like(self, user):  # continue
        if self.owner.isConnected:
            self.like_count += 1
            if user != self.owner:
                Users.notification.append(self.like_count)

    def comment(self, user, content):
        if self.owner.isConnected:
            self.comments.append(user, content)
            if user != self.owner:
                Users.notification.append(self.like_count)

    @abstractmethod
    def print_info(self, user):
        pass
