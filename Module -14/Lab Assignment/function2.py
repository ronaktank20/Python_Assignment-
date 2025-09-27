 #Write a Python program to create a calculator using functions. 

def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1-num2)

def mul(num1,num2):
    print(num1*num2)

def div(num1,num2):
    print(num1//num2)

def mdul(num1,num2):
    print(num1%num2)


while(True):

    print("1. for Addition")
    print("2. for subtraction")
    print("3. for multipication")
    print("4. for division")
    print("5. for moduls")
    choice = int(input("enter the choice :"))

    num1= int(input("enter the number 1 :"))
    num2= int(input("enter the number 2 :"))
    
    match choice:
        
        case 1:
            print(add(num1,num2)) 
        
        case 2:
            print(sub(num1,num2)) 
        
        case 3:
            print(mul(num1,num2)) 
        
        case 4:
            print(div(num1,num2)) 
        
        case 5:
            print(mdul(num1,num2))
              
        




        



