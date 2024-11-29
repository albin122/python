'''
Author: ALBIN PHILIP GIGI
Date : 29/11/2024
Description:Program to find the factorial of a number using Recursion
'''
def factorial(n):

    if n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=int(input( "enter the number "))
print("factorial of number=",factorial(n))                                    