def make_adder(k):
    def h(x):
        return k + x
    return h

adder_three = make_adder(3)
adder_ten = make_adder(10)

k = 5
print(adder_three(k))
print(adder_ten(k))

# Python tutor link:https://pythontutor.com/visualize.html#code=def%20make_adder%28k%29%3A%0A%20%20%20%20def%20h%28x%29%3A%0A%20%20%20%20%20%20%20%20return%20k%20%2B%20x%0A%20%20%20%20return%20h%0A%0Aadder_three%20%3D%20make_adder%283%29%0Aadder_ten%20%3D%20make_adder%2810%29%0A%0Ak%20%3D%205%0Aprint%28adder_three%28k%29%29%0Aprint%28adder_ten%28k%29%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# Concept: A function can return another function, and remembers the value of the variable k, even after the function make_adder has finished executing. This is called a closure.