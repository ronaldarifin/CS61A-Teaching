# In this file, we want to test if you understand the difference between an iterator and a generator.
# 1. Creating an iterator object by calling iter() on a list
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print("Iterator object:", my_iterator)
print("Type of iterator:", type(my_iterator))
print("Next value from iterator:", next(my_iterator))
print("List of iterator values:", list(my_iterator))

# 2. Creating a generator object by defining and calling a generator function
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print("\nGenerator object:", gen)
print("Type of generator:", type(gen))
print("Next value from generator:", next(gen))
print("List of generator values:", list(gen))

# 3. Using the map() function which returns a map object (iterator)
def square(x):
    return x * x

mapped_result = map(square, my_list)
print("\nMap object:", mapped_result)
print("Type of map object:", type(mapped_result))
print("List of mapped values:", list(mapped_result))

https://pythontutor.com/render.html#code=%23%20In%20this%20file,%20we%20want%20to%20test%20if%20you%20understand%20the%20difference%20between%20an%20iterator%20and%20a%20generator.%0A%23%201.%20Creating%20an%20iterator%20object%20by%20calling%20iter%28%29%20on%20a%20list%0Amy_list%20%3D%20%5B1,%202,%203%5D%0Amy_iterator%20%3D%20iter%28my_list%29%0Aprint%28%22Iterator%20object%3A%22,%20my_iterator%29%0Aprint%28%22Type%20of%20iterator%3A%22,%20type%28my_iterator%29%29%0Aprint%28%22Next%20value%20from%20iterator%3A%22,%20next%28my_iterator%29%29%0Aprint%28%22List%20of%20iterator%20values%3A%22,%20list%28my_iterator%29%29%0A%0A%23%202.%20Creating%20a%20generator%20object%20by%20defining%20and%20calling%20a%20generator%20function%0Adef%20my_generator%28%29%3A%0A%20%20%20%20yield%201%0A%20%20%20%20yield%202%0A%20%20%20%20yield%203%0A%0Agen%20%3D%20my_generator%28%29%0Aprint%28%22%5CnGenerator%20object%3A%22,%20gen%29%0Aprint%28%22Type%20of%20generator%3A%22,%20type%28gen%29%29%0Aprint%28%22Next%20value%20from%20generator%3A%22,%20next%28gen%29%29%0Aprint%28%22List%20of%20generator%20values%3A%22,%20list%28gen%29%29%0A%0A%23%203.%20Using%20the%20map%28%29%20function%20which%20returns%20a%20map%20object%20%28iterator%29%0Adef%20square%28x%29%3A%0A%20%20%20%20return%20x%20*%20x%0A%0Amapped_result%20%3D%20map%28square,%20my_list%29%0Aprint%28%22%5CnMap%20object%3A%22,%20mapped_result%29%0Aprint%28%22Type%20of%20map%20object%3A%22,%20type%28mapped_result%29%29%0Aprint%28%22List%20of%20mapped%20values%3A%22,%20list%28mapped_result%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false