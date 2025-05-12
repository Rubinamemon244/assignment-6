### 3. **Public Variables and Methods**
#Create a class `Car` with a public variable `brand` and a public method `start()`. Instantiate the class and access both from outside the class.**bold text**

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The car {self.brand} has been started")

car1 = Car("Lambhorgini")
car2 = Car("Toyota Fortuner")
car1.start()
car2.start()
