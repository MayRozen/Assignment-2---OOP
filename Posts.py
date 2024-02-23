from abc import ABC, abstractmethod


class Posts(ABC):
    _like = []

    def __init__(self, user):
        self._user = user


    def like(self, user):
        if user != self._user and user not in self._like:
            print(self._user)
            self._user.notification.append(f"{user.username()} liked your post")
            print(f"notification to {self._user.username()}: {user.username()} liked your post")

    def comment(self, user, content):
        if user != self._user:
            self._user.notification.append(f"{user.username()} commented on your post")
            print(f"notification to {self._user.username()}: {user.username()} commented on your post: {content}")

    @abstractmethod
    def print_info(self, user):
        pass

