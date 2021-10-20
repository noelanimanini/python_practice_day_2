# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# imported the random package
import random 
# created a variable that takes in the input for the names of the given string
names_string = input("what are the names.  ")
# split the string from the input 
names = names_string.split(",")
# print the names from the string 
print(names)
# randomize the list of the list of names
answer = random.randint(0, len(names))
# print the names in the sentence of who is paying for the bill
print(f"{names[answer]} is paying for the bill ")