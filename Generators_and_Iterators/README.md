# Concepts Checks

## Generators

The examples try to make you understand the differences between iterators, iterables, and generators. Some questions that may be helpful include:

- Do some active recall before looking at the answers!
- Are iterators also iterables?
- What is the difference between iterators and iterables?
- [Optional] Why do functions like `map`, `filter` take in an iterable? (since, it takes in an iterable we can also pass in an iterator)
- What is a generator? Is a generator an iterator? Is it an iterable too?
- Can we call `next` on a generator?

### Answers:

1. **Iterators are also iterables.**
2. Iterators are just pointers to the iterable value it is currently iterating (generalized). In a more detailed setting is because iterators have the `__next__` method that returns the next value in the iterator.
3. **Why do functions like map, filter, etc. take in an iterable and return an iterator?**
   It's because it wants to be efficient and not compute unless the program asks for it. If I do `map`, `filter`, `zip`, etc, it will only be more efficient on memory to be computed on the fly.
4. A generator is an iterator, but more advanced because you can do a whole bunch of things in the generator function.
5. Yes, we can call `next` on a generator because a generator is an iterator, so it has properties of iterators and iterables.

## WWPD (What Would Python Do) Check

### List Operations

Here we want to check and test the differences between slicing, concatenating, or references to the list object. A major thing in this example is, does concatenating a list that has a reference to another list make a copy?

**Note**: No, it still has the reference to it, so modifying the referenced list will modify this recently concatenated list.

### WWPD Links:

- [generators.py](https://pythontutor.com/visualize.html#code=def%20ronald_students_staff%28%29%3A%0A%20%20%20%20yield%28%22Adam%22%29%0A%20%20%20%20yield%28%22Shahad%22%29%0A%20%20%20%20yield%28%22Mihir%22%29%0A%20%20%20%20yield%28%22Morgan%22%29%0A%20%20%20%20yield%28%22Sammith%22%29%0A%20%20%20%20yield%28%22Sophie%22%29%0A%0A%0Adef%20ronald_students_csm%28%29%3A%0A%20%20%20%20yield%28%22Alberto%22%29%0A%20%20%20%20yield%28%22Hector%22%29%0A%20%20%20%20yield%28%22Isha%22%29%0A%20%20%20%20yield%28%22Rajoshi%22%29%0A%20%20%20%20yield%28%22Xing%20Sheng%22%29%0A%0A%23%20Since%20a%20generator%20is%20an%20iterator,%20we%20can%20call%20next%20on%20it.%0Astudent_iter%20%3D%20ronald_students_staff%28%29%0Aprint%28next%28student_iter%29%29%20%0Aprint%28next%28student_iter%29%29%20%20%0Aprint%28next%28student_iter%29%29%20%20%0Aprint%28next%28student_iter%29%29%20%0Aprint%28next%28student_iter%29%29%0Aprint%28next%28student_iter%29%29%0A%0A%23Since,%20we%20have%20a%20generator%20is%20a%20iterator,%0A%23%20we%20can%20loop%20through%20it%20using%20a%20for%20loop%20YAY!%0A%23%20BUT,%20have%20we%20used%20up%20our%20iter%3F%20So,%20can%20we%20do%20a%20loop%3F%0Aprint%28%22THIS%20IS%20WITH%20A%20LOOP%22%29%0Afor%20elem%20in%20student_iter%3A%0A%20%20%20%20print%28elem%29%0Aprint%28%22At%20this%20wonky%20loop,%20we%20didn%27t%20print%20anything%22%29%0A%0Aprint%28%22THIS%20IS%20WITH%20A%20LOOP,%20BUT%20NOT%20WONKY%22%29%0Afor%20elem%20in%20ronald_students_staff%28%29%3A%0A%20%20%20%20print%28elem%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

- [lists.py](https://pythontutor.com/visualize.html#code=one_item%20%3D%20%5B1%5D%0Atwo_item%20%3D%20%5B4,5%5D%0A%0A%23%20Multiple%20ways%20to%20make%20a%20whole%20new%20copy%20of%20a%20list.%0Anew_list_one%20%3D%20one_item%20%2B%20%5B%5D%0Anew_list_two%20%3D%20list%28one_item%29%0Anew_list_three%20%3D%20one_item%5B%3A%5D%0A%0A%23%20This%20is%20not%20a%20new%20copy,%20%0A%23%20so%20we%20are%20mutating%20the%20list%20if%20we%20do%20this%0Arefered_list_one%20%3D%20one_item%0A%0Anested_list_reference%20%3D%20%5Bone_item%5D%20%2B%20%5Btwo_item%5D%0Atwo_item.pop%28%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
