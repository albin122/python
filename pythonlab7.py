'''
Author :Albin Philip Gigi
Date : 19/10/2024
Descrpition :a Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
        Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''


first_name = input("enter your first name")
last_name =input("enter your last name")
name = first_name+" "+last_name
print(name)
print(len(first_name))
first_name_length=len(first_name)
extracted_name_length=name[first_name_length+1:]
print(extracted_name_length)