# Deque tutorial Python

# Deque is a double-ended queue. It can be used to add or remove elements from both ends.

dq = deque([1,2,3,4,5])
print(dq)

# Adding elements to the right end
dq.append(6)
print(dq)

# Adding elements to the left end
dq.appendleft(0)
print(dq)

# Removing elements from the right end
dq.pop()
print(dq)

# Removing elements from the left end
dq.popleft()
print(dq)

# Accessing elements
print(dq[0])
print(dq[-1])

# Length of the deque
print(len(dq))

# Clearing the deque
dq.clear()

# Deque can also be used as a stack
dq.append(1)
dq.append(2)
dq.append(3)