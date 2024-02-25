from enum import Enum

from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class PostType(Enum):
    TEXTPOST = 'Text'
    IMAGEPOST = 'Image'
    SALEPOST = 'Sale'


class FactoryPosts:

    @staticmethod
    def created_post(post_type, user, *content):
        if post_type == PostType.TEXTPOST:
            new_post = TextPost(user, *content)
            return new_post
        elif post_type == PostType.IMAGEPOST:
            new_post = ImagePost(user, *content)
            return new_post
        elif post_type == PostType.SALEPOST:
            new_post = SalePost(user, *content)
            return new_post
        else:
            raise ValueError("Invalid post type")
