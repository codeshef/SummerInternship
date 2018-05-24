

# Introduction to set

# Create empty set

x = set()

print(x)

# Create non empty set (Can also be declared using {} if unique value is added otherwise it is considered as dictionary)
n = set([0, 1, 2, 3])
print(n)


# A new empty set

color_set = set()
color_set.add('Red')
print(color_set)

# update set by adding multiple values

color_set.update(["Blue", "Green"])
print(color_set)

# In case of repeated value
color_set.add('Red')
print(color_set)

# Remove from set(pop first value)

n.pop()
print(n)

# To pop particular index use remove or discard
# remove throw exception whereas discard doesn't in case of unknown

n.discard(5)
print(n)

# Error in case of removing unknown value
#n.remove(5)
#print(n)

