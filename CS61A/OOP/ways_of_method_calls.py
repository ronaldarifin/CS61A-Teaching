class MyClass:
    def instance_method(self, message):
        print(f"Instance method called with message: {message}")

# Creating an instance of MyClass
my_instance = MyClass()

# Calling the instance method using the instance
my_instance.instance_method("Hello using instance")

# Calling the instance method directly from the class, passing the instance as the first argument
MyClass.instance_method(my_instance, "Hello using class")
