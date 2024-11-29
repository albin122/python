def phn_number():
    num=input("enter phone number")
    if len(num)==10 and num[0] in ["9","8","7"]:
       print("VALID NUMBER")
    else:
        print("NOT VALID NUMBER")
phn_number()
