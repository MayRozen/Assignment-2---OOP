from abc import ABC, abstractmethod


class Posts(ABC):
    _like = []

    def __init__(self, user):
        self._owner = user

    def like(self, user):
        if user != self._owner and user not in self._like:
            self._owner.notification.append(f"{user.username()} liked your post")
            print(f"notification to {self._owner.username()}: {user.username()} liked your post")

    def comment(self, user, content):
        if user != self._owner:
            self._owner.notification.append(f"{user.username()} commented on your post")
            print(f"notification to {self._owner.username()}: {user.username()} commented on your post: {content}")
