### 6. **Constructors and Destructors**  
#Create a class `Logger` that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("New object created.")

    def __del__(self):
        print("New object destroyed.")

# Object creation
log = Logger()

# Optional: force deletion
del log
