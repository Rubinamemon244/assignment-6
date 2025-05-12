# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print(f"Deleting price {self.name}")
        del self._price

product = Product("Laptop", 50000)
print(product.price)      # Output: 50000

product.price = 48000     # OK
print(product.price)     # Output: 1200
product.price = -500    # Will print warning

del product.price         # Deletes _price
