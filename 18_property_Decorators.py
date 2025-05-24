class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)       # Get price
p.price = 150        # Update price
print(p.price)
del p.price          # Delete price
