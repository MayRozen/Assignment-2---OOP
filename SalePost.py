from Posts import Posts


class SalePost(Posts):

    def __init__(self, user, description, price, location):
        super().__init__(user)
        self._description = description
        self._price = price
        self._location = location
        self._available = True

    def discount(self, percentage, password):
        if self._owner.password() == password:
            if 0 <= percentage <= 100:
                discount_amount = self._price * (percentage / 100)
                discounted_price = self._price - discount_amount
                self._price = discounted_price
                print(f"Discount on {self._owner.username()} product! the new price is: {self._price}")
            else:
                print("Invalid discount percentage. It should be between 0 and 100.")

    def sold(self, password):
        if self._owner.password() == password:
            self._available = False
            print(f"\n{self._owner.username()}'s product is sold")
            self.__str__()


    def __str__(self):
        if self._available:
            text = "For sale!"
        else:
            text = "Sold!"

        a = f"{self._owner.username()} posted a product for sale:\n"
        b = f"{text} {self._description}, price: {self._price}, pickup from: {self._location}\n"
        return a+b
