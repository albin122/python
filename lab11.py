'''
Author :Albin Philip Gigi
Date : 25/10/2024
Descrpition :a Python program to find the largest of three numbers.
 The program should take three numbers as input from the user and determine which one is the largest.
 Use conditional statements to compare the numbers.
'''
number1=int(input("enter  first number"))
number2=int(input("enter second number"))
number3=int(input("enter third number"))
if number1>number2 and number1>number3:
    print(number1, " is graeter than the other two")
elif number2>number3:
    print(number2,"is graeter than the other two")
else:
    print(number3,"is graeter than the other two")

