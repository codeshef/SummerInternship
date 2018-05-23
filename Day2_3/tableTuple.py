# Print tables of number using

tp = tuple(input("Input numbers"))

#print(type(tp))

#print(tp)

for i in tp:
    print(i + " table ")
    for j in range(1, 11):
        result = int(i)*j
        print(result)


