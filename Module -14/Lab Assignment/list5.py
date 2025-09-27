#Write a Python program to insert elements into an empty list using a for loop and 
#append(). 


lst = []

n=int(input("how many element do you want to insert :"))

for i in range(n):
    element = input("Enter element :")
    lst.append(element)

print(lst)

