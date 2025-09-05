#Practical Example 3: Write a Python program to find a specific string in the list using a simple 
#for loop and if condition. 
flag=1
lst=["milk","tea","coffie"]
search_str= input("enter the str :")
for i in lst:
    if i==search_str:
        flag=0
        break

if flag==1:
    print(f"{search_str} Not Avaliable in the list")
else :
    print(f"{search_str} Avaliable in the list")

