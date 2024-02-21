import Posts


class ImagePost(Posts):
    image = ""

    def __init__(self, image, owner, like_count, comments):
        super().__init__()
        self.image = image
        super().__init__(owner, like_count, comments)

    def display(self):
        display_image = Image.open(self.image)
        display_image.show()

    def print_info(self):
        image_string = "imagePost"
        print(f"{self.owner.name} {Posts.create_post(image_string, self.owner, self.image).display()}")
