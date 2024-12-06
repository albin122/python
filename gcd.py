def gcd(num1,num2):
    if num1 % num2 == 0:
        return num2
    else:
       return gcd(num2,num1%num2)
num1=int(input("enter a number"))
num2=int(input("enter a number"))

print(gcd(num1,num2))