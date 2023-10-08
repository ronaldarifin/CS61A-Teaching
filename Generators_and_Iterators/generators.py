def ronald_students_staff():
    yield("Adam")
    yield("Shahad")
    yield("Mihir")
    yield("Morgan")
    yield("Sammith")
    yield("Sophie")


def ronald_students_csm():
    yield("Alberto")
    yield("Hector")
    yield("Isha")
    yield("Rajoshi")
    yield("Xing Sheng")

# Since a generator is an iterator, we can call next on it.
student_iter = ronald_students_staff()
print(next(student_iter)) 
print(next(student_iter))  
print(next(student_iter))  
print(next(student_iter)) 
print(next(student_iter))

#Since, we have a generator is a iterator,
# we can loop through it using a for loop YAY!
# BUT, have we used up our iter? So, can we do a loop?
print("THIS IS WITH A LOOP")
for elem in student_iter:
    print(elem)
print("At this wonky loop, we didn't print anything")

print("THIS IS WITH A LOOP, BUT NOT WONKY")
for elem in ronald_students():
    print(elem)