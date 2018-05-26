# List

l = list() #or l=[]

# to get type

print(type(l))

print(len(l))

l = ['a', 'b', 'c', 45, 5.6, True]

# print entire list

print(l)

# print using slicing

print(l[1:4])

# print without starting point

print(l[:4])

# print without ending point

print(l[3:])

# print using for loop

for i in l:
    print(i)

# delete index of  list

del l[0]
print(l)

# function append , extend ,insert,remove,pop

# insert value at index

l.insert(0, 'z')
print(l)

# append  entire list at particular index and extend every element get unique index
l.append(['z', 'x', 'y'])
print(l)

l.extend(['z', 'x', 'y'])
print(l)

# Remove exact value pop index
l.remove('z')
l.pop(5)
print(l)