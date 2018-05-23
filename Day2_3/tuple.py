# Tuple in python

t =() # or tuple()

# add data into tuple
t=('v','g',5,6.6,True)

a = "b","b","m","n"

print(type(t))

print(type(a))

# access method same as list

#unpacking of tuple

tuplex = ("b", 4, False)
n1, n2, n3 = tuplex
print(n1, n2, n3)


# Find repeated values using count function

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex)
count = tuplex.count(4)
print(count)

# To check whether element is present or not

print(5 in tuplex)

# convert direct into string from tuple using join function

tup = ('e', 'x', 'e', 'r', 'c', 'i')
str =''.join(tup)
print(str)

#negative index

item1 = tuplex[-4]

print(item1)

item1 = tuplex[: -1]
print(item1)

# create another tuple

tuplex = tuple("Hello World")
print(tuplex)

_slice = tuplex[2:9:2]
print(_slice)

# Return a tuple with jump every 3 items
_slice = tuplex[::4]
print(_slice)
# Back track

_slice = tuplex[9:2:-4]
print(_slice)

# Index finding
index = tuplex.index("l")
print(index)

# define index from which we want to search
index = tuplex.index("l", 4)
print(index)

# Define range and find index
index = tuplex.index("l", 3, 6)
print(index)

