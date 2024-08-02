# here we are using len func 
# to check the length of the name 
# len func count the spaces as well
names = "mehraj"
length=len(names)
print(f"length of your name is {length}")

# lower method 
# use to make the alphabets in small letter
user = 'merhaj'
print(user.lower())

# upper method
# this method makes the character in caps
print(user.upper())
# title method
# this method make the first letter in caps
print(user.title())
# count method
# this method use for count and write the word in parenthesis that what you have to count 
print(user.count("h"))
# strip method
# use to remove spaces
s='   mehraj   '
print((s).lstrip()) #use to remove lefttside space
print((s).rstrip()) # use to remove rightside space
print(s.strip()) #remove both spaces
# if there is more space than we use replace method.

# exercise
name, chac = input("enter comma seprated name and chacracter :").split(",")
print(f"character count : {name.strip().lower().count(chac.strip().lower())}")
print((name))




