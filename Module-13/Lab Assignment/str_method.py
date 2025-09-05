# Write a Python program that manipulates and prints strings using various string methods.

str = "    Tops technologies       "

print("String:",str)


print("strip() ", str.strip())


print("lower() ",str.lower())


print("upper()", str.upper())


print("capitalize() ",str.capitalize())


print("replace('technologies', 'tech')", str.replace("technologies", "tech"))


print("find('Tops') ", str.find("Tops"))


print("split() ", str.split())


words = ["Hello", "World"]
print("' '.join(words) →", " ".join(words))