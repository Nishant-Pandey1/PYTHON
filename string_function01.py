# Modify means changing it's property




a = "Technology"
print("In capital : ",a.upper())
print("In Lower     :",a.lower())
print("Replacing o with i in technology",a.replace("o","i"))
  
#If two words are in same string value, we can split it
a = "United . States"
print(a.split("."))


# concatinationing a string
a = "United"
b = "States"
c = a + " " + b
print(c)


#formating a string 
age = input("Enter your age: ")
name = input("Your name: ")
result = "Hi, I know you're {} and you're {} years old"
print(result.format(name , age))


