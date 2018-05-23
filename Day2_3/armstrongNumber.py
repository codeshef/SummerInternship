
#  Dynamic armstrong number


n = (input("Enter any number"))
l = len(n)
# print(l)
n = int(n)

number = n
sum =0

rem =0

while(n>0):
    rem = n%10
    power = rem**(l-1) #(** for power function)
    #print(power)
    sum+=power
    n =n//10 #(// for typecast into int)
if(sum == number):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")