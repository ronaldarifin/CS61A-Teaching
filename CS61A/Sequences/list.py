a = [1,2,3]
b = a
# EXAMPLE:
# we modify in place
# a += [4]
# we create a new list object
# a = a + [4]
# we create a new list where the inner a refers to the original a
# a = a + [a]
# we create a list where the a is concatenated and is not a referal
# a = a + a
# so what does this do?
a = a + [4, [5,6]]
c = a
# we emphasize that a pointer still remembers unless everyone forgets it
a = [4,5]
# EXAMPLE:

# WHEN WE +=, we make a POINTER
# WHEN WE = +, we make a COPY, except the items in it.
# WHEN WE ASIGN, we make a pointer
# WHEN WE SLICE, we make a COPY
# WHEN we reasign, all previous pointers still remember

d = c[3:5]
c[3] = 9

# https://pythontutor.com/visualize.html#code=a%20%3D%20%5B1,2,3%5D%0Ab%20%3D%20a%0A%23%20EXAMPLE%3A%0A%23%20we%20modify%20in%20place%0A%23%20a%20%2B%3D%20%5B4%5D%0A%23%20we%20create%20a%20new%20list%20object%0A%23%20a%20%3D%20a%20%2B%20%5B4%5D%0A%23%20we%20create%20a%20new%20list%20where%20the%20inner%20a%20refers%20to%20the%20original%20a%0A%23%20a%20%3D%20a%20%2B%20%5Ba%5D%0A%23%20we%20create%20a%20list%20where%20the%20a%20is%20concatenated%20and%20is%20not%20a%20referal%0A%23%20a%20%3D%20a%20%2B%20a%0A%23%20so%20what%20does%20this%20do%3F%0Aa%20%3D%20a%20%2B%20%5B4,%20%5B5,6%5D%5D%0Ac%20%3D%20a%0A%23%20we%20emphasize%20that%20a%20pointer%20still%20remembers%20unless%20everyone%20forgets%20it%0Aa%20%3D%20%5B4,5%5D%0A%23%20EXAMPLE%3A%0A%0A%23%20WHEN%20WE%20%2B%3D,%20we%20make%20a%20POINTER%0A%23%20WHEN%20WE%20%3D%20%2B,%20we%20make%20a%20COPY,%20except%20the%20items%20in%20it.%0A%23%20WHEN%20WE%20ASIGN,%20we%20make%20a%20pointer%0A%23%20WHEN%20WE%20SLICE,%20we%20make%20a%20COPY%0A%23%20WHEN%20we%20reasign,%20all%20previous%20pointers%20still%20remember%0A%0Ad%20%3D%20c%5B3%3A5%5D%0Ac%5B3%5D%20%3D%209&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false