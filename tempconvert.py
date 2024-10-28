while True:
    print("1,\tConvert Celsius to Fahrenheit")
    print("2,\tConvert Fahrenheit to Celsius")
    print("3,\tExit the program")
    choice=int(input("enter the choice"))
    if choice==1:
        temperature=float(input("enter the temperature in celsius"))
        print("temperature in fahrenheit=",(temperature*9/5)+32)
    elif choice==2:
        temperature2=float(input("enter the temperature in fahrenheit"))
        print("temperature in celsius=",(temperature2-32)*5/9)
    elif choice==3:
        break
        print("exit the program")
    else:
        print("incorrect Entry")
