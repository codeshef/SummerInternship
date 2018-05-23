
# Reverse digits using mathematical formula

print("Using mathematical formula")

n = int(input("Enter any number"))

sum =0

rem =0

while(n>0):
    rem = n%10
    sum=sum*10+rem
    n =n//10
print(sum)

