# here we use replace method
# we can replace word with other word
# if there are two same words than we use number that how many words that we have to replace  
# we have to write the position number.


string="she is beautiful and she is a good dancer"
print(string.replace("is","was" , 2))
print(string.replace(" ","_"))

# find method
# use to find particular word or character.
# to know the position of the words
# if there are two same words than we use number that how many words that we have to replace 
# we have to write the position number
# we can make variable as well to find the word

print(string.find("is"))
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)
