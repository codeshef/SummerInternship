
# given string by user we have to count number of vowels

str = input("Enter string")
vowels = ['a','e','i','o','u']
count=0

for i in str:
    for j in vowels:
        if(i==j):
            count+=1
print(count)

