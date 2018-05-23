# sum of digits

# logic let n=678 ,n%10 = 8(give reminder),n/10 = 67(give quotient)

n = int(input("Enter any number"))

sum =0

rem =0

while(n>0):
    rem = n%10
    sum+=rem
    n =n//10
print(sum)