'''
Author: ALBIN PHILIP GIGI
Date : 29/11/2024
Description:A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle,
  the square of one side equals the sum of the squares of the other two sides). Implement using functions.
'''
def triangle():
    l1=[]
    side1=int(input("enter first side of triangle"))
    l1.append(side1)
    side2=int(input("enter second side of triangle"))
    l1.append(side2)
    side3=int(input("enter third  side of triangle"))
    l1.append(side3)
    l1.sort()
    if l1[2]**2==l1[1]**2+l1[0]**2:
        print("it is a right angled triangle")
    else:
        print("it is not a right angled triangle")
triangle()
