# Example of Short Circuiting

# Truth Table for AND
# 1 and 1 = 1
# 1 and 0 = 0
# 0 and 1 = 0
# 0 and 0 = 0

# A simple logic is that whenever we find a False [0], we know that it's false. So we can stop checking the rest of the conditions.
# This means AND short circuits when it finds a False value.

# Code Example:
print(1 and 2 and 3) # 3
print(1 and 0 and 3) # 0


# Example of Short Circuiting

# Truth Table for OR
# 1 or 1 = 1
# 1 or 0 = 1
# 0 or 1 = 1
# 0 or 0 = 0

# A simple logic is that whenever we find a True [1], we know that it's true. So we can stop checking the rest of the conditions.
# This means OR short circuits when it finds a True value.

# Code Example:
print(1 or 2 or 3) # 1
print(1 or 0 or 3) # 1
print(0 or 0 or 3) # 3

# Falsy values in python are: 0, False, None, [], '', 0.0
