name= "mehraj"
print(name.center(10, "*"))
name=input("enter ypur name : ")
print(name.center(len(name)+8,"*"))
print(type(name))
#  we use this method to add some fun thing beside our names
# in that we have to add the stars(*) or anything you want to add
# and add how many you want to add excluding string length for ex:
# mehraj--->length is 6 and i have add 4 stars beside mehraj.hence, i will 10 --->4+6
# if you dont the length of your string use len func 