# find the largest and min values of a list. No min() or max()

# create the input question 
question = input(" List all the scores from the students and place a comma after each score! ").split(",")

#create two variables that represent the min and the max and set both equal to 0
min = 0
max = 0 
# print(question)
# loop through the list and convert each iteration to an integer. 
for score in question: 
  curr = int(score)
  if curr > max:
    max = curr
print(f"the height score in the class is {max}")
