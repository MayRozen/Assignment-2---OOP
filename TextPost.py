import Posts


class TextPost(Posts):
    text = ""

    def __init__(self, text, owner, like_count, comments):
        super().__init__()
        self.text = text
        super().__init__(owner, like_count, comments)

    def print_info(self):
        print(f"{self.text} {self.owner.name}")
