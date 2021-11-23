#  1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# create a file that processes the number of cans we need to buy. Given any height or any width, 
# multiply the height by the width and divide it by the coverage (5). 
import math

height_input = input("What's the height? ")
width_input = input("What's the width? ") 
coverage = 5 

def paint_calc(height=height_input , width=width_input, coverage=5):
  h = int(height)
  w = int(width)
  ans = (h * w) / coverage 
  print(math.ceil(ans))

paint_calc(height_input,width_input,coverage)