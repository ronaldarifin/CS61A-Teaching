one_item = [1,[100,200]]
two_item = [4,5,[1000]]

# Multiple ways to make a whole new copy of a list.
# Observe the references. new_list_one still points to the inner list of one_item.
new_list_one = one_item + []
new_list_two = list(one_item)
new_list_three = one_item[:]
nested_list_reference = [one_item] + [two_item]


# This is mutation. Not a new list.
refered_list_one = one_item
# does this mutate the origianl list?
refered_list_one += [1000]

two_item.pop()