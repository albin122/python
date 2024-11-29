'''
Author: ALBIN PHILIP GIGI
Date : 29/11/2024
Description:Program to check whether the given number is a valid mobile number or not using functions.

Rules:
    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
'''
def phn_number():
    num=input("enter phone number")
    if len(num)==10 and num[0] in ["9","8","7"]:
       print("VALID NUMBER")
    else:
        print("NOT VALID NUMBER")
phn_number()
