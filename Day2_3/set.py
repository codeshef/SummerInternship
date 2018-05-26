

# Introduction to set

# Create empty set

import ntpath

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

# Intersection
setx = set(["green", "blue"])
sety = set(["green", "red"])
setz = setx & sety
print("Intersection ", setz)

# Union
setz = setx | sety
print("Union ", setz)

# set difference (different value of set from which we subtract)
setz = setx - sety
print("Set difference ", setz)

# Symmetric difference (Different values from both set)
setz = setx ^ sety
print("Symmetric Difference ", setz)

#  superset or subset

x = set(["a", "b", "c"])
y = set(["a", "c"])
z = set(["a"])

isSubset = y <= x
print(isSubset)

isSuperset = y >= x
print(isSuperset)

issubset = z <= y
print(isSubset)

isSuperset = z >= y
print(isSuperset)

# Cpy and clear

setw = x.copy()
print(setw)

setw.clear()
print(setw)

# Max or min

print("Maximum ", max(n))
print("Minimum ", min(n))

print(set("The The The".split()))


# Separate fileName and ext using split()

s = "abc.txt"
name, ext = s.split(".")
print(name, ext)

# Separate fileName from path using ntpath module
s = "/home/anchal/Desktop/userDirectory/anchal/userFile.txt"
fullpath, filename = ntpath.split(s)
print("FullPath : ", fullpath)
print("Filename : ", filename)
name, ext = filename.split('.')
print("name : ", name)
print("ext  : ", ext)







