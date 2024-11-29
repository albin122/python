'''
Author: ALBIN PHILIP GIGI
Date : 29/11/2024
Description:Recursive function to add two positive numbers.
'''
def add(num1,num2):
     if num2==0:
         return num1
     else:
         return add(num1+1,num2-1)
num1=int(input(" enter the number 1 "))
num2=int(input("enter the number 2 "))
add(num1,num2)
print(add(num1,num2))