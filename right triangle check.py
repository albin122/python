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
