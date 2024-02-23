from Posts import Posts


class TextPost(Posts):

    def __init__(self, text, user):
        super().__init__(user)
        self.text = text

    def print_info(self):
        print(f"{self.text} {self._user.name}")
        
