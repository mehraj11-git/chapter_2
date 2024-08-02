# string
name = "mehraj"

print(name)
# string indexing
print(name [2])
# string slicing
print(name[0:3])
# take user input
name1 =input("enter your name : ")
print(name1)
# take two user inputs
name2,age= input("enter your name and age").split(",")
print(name2)
print(age)
# len function
print(len(name))
# lower,title,upper ,count method
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("2"))
# strip method
print(name.strip())
# find,replace,center method
print(name.find("h"))
print(name.replace("h","H"))
print(name.center(10, "*"))
# strings are immutable
print(name[2])
# more operators
name3 = "mehr"
name3 += "aj"
print(name3)
print(type(name3))