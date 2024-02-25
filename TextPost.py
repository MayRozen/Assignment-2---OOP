from Posts import Posts


class TextPost(Posts):

    def __init__(self, user, text):
        super().__init__(user)
        self._text = text

    def __str__(self):
        a = f"{self._owner.username()} published a post:\n"
        b = f"\"{self._text}\"\n"

        return a+b
