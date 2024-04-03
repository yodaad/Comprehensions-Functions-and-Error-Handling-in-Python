# Operations with sets in Python are similar to those in mathematics. The following are some of the operations that can be performed with sets in Python:

set_a = {"col", "mex", "bol"}
set_b = {"per", "bol"}

# Union (returns a new set with all elements from both sets)
set_c = set_a.union(set_b)
print(set_c)

# Using the pipe operator
print(set_a | set_b)

set_d = set_a | set_b
print(set_d)

# Intersection (returns a new set with elements that are common to both sets)
set_e = set_a.intersection(set_b)
print(set_e)

# Using the ampersand operator
set_f = set_a & set_b
print(set_f)

# Difference (returns a new set with elements in the first set that are not in the second set)
set_g = set_a.difference(set_b)
print(set_g)

# Using the minus operator
set_h = set_a - set_b
print(set_h)

# Symmetric Difference (returns a new set with elements that are in either of the sets, but not both)
set_i = set_a.symmetric_difference(set_b)
print(set_i)

# Using the caret operator
set_j = set_a ^ set_b
print(set_j)