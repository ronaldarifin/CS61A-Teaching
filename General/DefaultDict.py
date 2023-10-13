from collections import defaultdict

# Creating a defaultdict with int as the default factory
d = defaultdict(int)

# Inserting data
d['apple'] = 10
d['banana'] = 5

# Accessing data
print(d['apple'])    # Output: 10
print(d['banana'])   # Output: 5
print(d['nothing here'])

d['apple'] += 3
d['orange'] += 1

print(d)

print("\n\nhow to print all element i dict")
for key in d:
    print(f'This is the key {key} and the value is {d[key]}')


