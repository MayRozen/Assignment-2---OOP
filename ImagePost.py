from Posts import Posts
import matplotlib.pyplot as plt


class ImagePost(Posts):

    def __init__(self, user, image_post):
        super().__init__(user)
        self._image_post = image_post

    def display(self):
        display_image = plt.imread(self._image_post)
        plt.imshow(display_image)
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def __str__(self):
        a = f"{self._owner.username()} posted a picture\n"
        return a
