class Parent:
    parent_attribute = "I'm a parent attribute"

class Child(Parent):
    child_attribute = "I'm a child attribute"

# Creating an instance of Child
child_instance = Child()

# Accessing an attribute present in the parent class
print(child_instance.parent_attribute)  # Output: I'm a parent attribute

# Accessing an attribute that is not present in either class will raise an AttributeError
# print(child_instance.non_existent_attribute)  # This will raise an AttributeError
