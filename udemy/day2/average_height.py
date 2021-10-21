# using a for loop, calculate the average height
# cannot use len() or sum()

# create a question that inputs the students heights
question = input(" list all of the students height and put a comma after each height. ").split(", ")
# initialize a variable 
ans = 0
# initialize a variable to count the length of the list 
length = 0
# loop through the list
for student in question:
  length += 1
  # convert from a string into an integer and add it to a variable
  ans += int(student)

# coming out of the for loop, now calculate the average 
result = round(ans/length)
# print the result in the form of an answer
print(f"{result} is the average height of all the students! ")

