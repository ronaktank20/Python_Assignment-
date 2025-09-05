#Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
#using a nested if.

age = int(input("enter the age: "))

if age>18:
    if age>=18 and age<=60:
        print("eligible to donate blood")
    else:
        print("not eligible to donate blood")
else:
    print("not eligible to donate blood")