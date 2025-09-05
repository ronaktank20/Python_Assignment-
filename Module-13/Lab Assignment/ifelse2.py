# Practical Example 6: Write a Python program to check if a number is prime using if_else. 
flag=1
num=int(input("enter the number :"))
for i in range(2,num):
    if(num%i==0):
        flag=0
if flag==1:
    print(f"{num} is prime") 
else:
    print(f"{num} is not a prime")    
