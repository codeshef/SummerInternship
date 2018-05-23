# dictionary

# empty value
d = {}

d["name"] = "Anchal"

print(type(d))
# print key-value pair
print(d)

# print value

print(d["name"])

# add values

d = {'n': 'a', 'b': 'v'}
# to get number of keys

print(d.keys())

# to get number of values

print(d.values())

# Making shallow copy of dictionary


# Iterating over dictionary
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for keys, values in d.items():
    print(keys, 'corresponds to', d[keys])

# Sum of all dictionary values
my_dic = {'data1': 100, 'data2': 200, 'data3': 300}
print(sum(my_dic.values()))

# Multiplication of all the values of dictionary
result = 1
for key in my_dic:
    result = result * my_dic[key]
print(result)

# del function same
del my_dic['data1']
print(my_dic)

# Add list into dictionary
# Add two list into dictionary using zip function
keys = ['red', 'green', 'blue']
values=['1', '2', '3']
dic_color = dict(zip(keys, values))
print(dic_color)

# Sorting keys in Dictionary (format to add values in keys)

for key in sorted(dic_color):
    print("%s : %s" % (key, dic_color[key]))  # sort according to key

# Getting maximum or minimum value from dictionary
number_dict = {'x': 100, 'y': 200, 'z': 50}
print(max(number_dict.values()))
print(min(number_dict.values()))

