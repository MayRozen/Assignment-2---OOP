from Posts import Posts


class SalePost(Posts):
    description = ""
    price = None
    location = ""
    available = False

    def __init__(self, description, price, location, owner, like_count, comments):
        self.description = description
        self.price = price
        self.location = location
        self.available = True
        super().__init__(owner, like_count, comments)

    @staticmethod
    def discount(self, percentage, password):
        if self.owner.password == password:
            if 0 <= percentage <= 100:
                discount_amount = self.price * (percentage / 100)
                discounted_price = self.price - discount_amount
                self.price = discounted_price
                print(f"new price after discount is {self.price}")
            else:
                print("Invalid discount percentage. It should be between 0 and 100.")

    def sold(self, password):
        if self.owner.password == password:
            self.available = False

    def print_info(self):
        print(f"it's {self.available} that the product of {self.owner.name} is sold")
