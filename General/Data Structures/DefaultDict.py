from collections import defaultdict

def printIterable(IterableName, iterable):
    print("\n\nhow to print all element i dict")
    for key in d:
        print(f'This is the key {key} and the value is {d[key]}')

d = defaultdict(int)

# Inserting data
d['chicken'] = 10
d['banana'] = 5

# Accessing data
print(d['chicken'])
print(d['banana'])
print(d['nothing here'])

# Modifying Data
d['chicken'] += 3
d['orange'] += 1

print("\n\nhow to print all element i dict")
for key in d:
    print(f'This is the key {key} and the value is {d[key]}')
# Iterating Data
