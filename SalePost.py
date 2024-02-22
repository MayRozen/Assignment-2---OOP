from Posts import Posts


class SalePost(Posts):

    def __init__(self, description, price, location, user):
        super().__init__(user)
        self.description = description
        self.price = price
        self.location = location
        self.available = True

    @staticmethod
    def discount(self, percentage, password):
        if self.user.password == password:
            if 0 <= percentage <= 100:
                discount_amount = self.price * (percentage / 100)
                discounted_price = self.price - discount_amount
                self.price = discounted_price
                print(f"new price after discount is {self.price}")
            else:
                print("Invalid discount percentage. It should be between 0 and 100.")

    def sold(self, password):
        if self._user.password == password:
            self.available = False

    def print_info(self):
        print(f"it's {self.available} that the product of {self._user.name} is sold")
