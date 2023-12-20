# Look up in sets is O(1) on average
# Example:
# Complexity: O(1)
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)
print(1 in s)
print(5 in s)

# Example of using sets to find unique elements in a list
# Complexity: O(n)
lst = [1,2,3,4,5,6,1,2,3]
unique = set(lst)
print(unique)

# Example of using sets to find common elements in two lists
# Complexity: O(n)
lst1 = [1,2,3,4,5] 
lst2 = [4,5,6,7,8]
common = set(lst1).intersection(lst2)
print(common)

