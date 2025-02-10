class ClassA:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from ClassA, {self.name}!"


class ClassB:
    def __init__(self, name):
        self.name = name
        # Creating an instance of ClassA
        self.class_a = ClassA(name)

    def call_greet_from_class_a(self):
        # Calling the greet method of ClassA
        return self.class_a.greet()


# Create an instance of ClassB
obj_b = ClassB("John")
# Calling the method from ClassA through ClassB
print(obj_b.call_greet_from_class_a())
