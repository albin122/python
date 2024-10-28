balance_amount=1000
while True:
    print("1,\tcheck balance")
    print("2,\tDeposit money")
    print("3,\twithdrawn money")
    print("4\texit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("balance",balance_amount)
    elif choice==2:
        deposit=int(input("enter amount to deposit"))
        print("balance:",balance_amount+deposit)

    elif choice==3:
        withdrawn_amount=float(input("enter amount to withdraw"))
        balance_currentamount=balance_amount-withdrawn_amount
        print("the amount withdrawn",withdrawn_amount,"current balance=",balance_currentamount)
    elif choice==4:
        break
        print("invalid entry")



