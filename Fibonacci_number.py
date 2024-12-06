def generate_fibonacci(n):
    list=[]
    num1=0
    num2=1
    for i in range(n):
        list.append(num1)
        num1,num2=num2,num1+num2
    return list

