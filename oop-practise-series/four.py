### 5. **Static Variables and Static Methods**  
#Create a class `MathUtils` with a static method `add(a, b)` that returns the sum. No class or instance variables should be used.

class Math:
    @staticmethod
    def Addition(a, b):
        return a + b

s1 = Math.Addition(2, 3)
print(s1)
