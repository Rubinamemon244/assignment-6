# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
     def __init__(self, engine_type):
         self.engine_type = engine_type

     def start(self):
         return f"Because {self.engine_type} engine is strating."

class Car:
     def __init__(self, brand, engine):
         self.brand = brand
         self.engine = engine

     def strat_car(self):
         return f"{self.brand} car is starting now. {self.engine.start()}"


engine = Engine("V8")
car = Car("Toyota" , engine)
print(car.strat_car())