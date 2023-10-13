one_item = [1]
two_item = [4,5]

# Multiple ways to make a whole new copy of a list.
new_list_one = one_item + []
new_list_two = list(one_item)
new_list_three = one_item[:]

# This is not a new copy, 
# so we are mutating the list if we do this
refered_list_one = one_item

nested_list_reference = [one_item] + [two_item]
two_item.pop()