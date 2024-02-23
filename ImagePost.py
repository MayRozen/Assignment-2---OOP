from Posts import Posts
import matplotlib.pyplot as plt


class ImagePost(Posts):

    def __init__(self, user, image_post):
        super().__init__(user)
        self.image_post = image_post

    def display(self):
        display_image = plt.imread(self.image_post)
        plt.imshow(display_image)
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def print_info(self):
        return f"{self._user.username()}"
        
