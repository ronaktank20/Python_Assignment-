#Write a Python program to merge two lists into one dictionary using a loop.

lst1 = [10,20,30]
lst2 = [40,50,60]
dict ={}

for i in range(len(lst1)):
    dict[lst1[i]]=[lst2[i]]

print(dict)

