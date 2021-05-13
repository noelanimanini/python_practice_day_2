print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: 
  print("You can ride the rollercoaster")
else: 
  print("sorry you have to grow taller before you ride.")

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if number % 3 == 1:
  print("this is an odd number")
else:  
  print("this is an even number")

  height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_height = float(height)
new_weight = float(weight)
result = round(new_weight / (new_height ** 2))

if result < 18.5: 
  print(f"your BMI is {result}, you are underweight")
elif 25 > result > 18.5: 
  print(f"your BMI is {result}, you have normal weight")
elif 30 > result > 25: 
  print(f"you are slightly overweight")
elif 35 > result > 30: 
  print(f"you are obese")
elif result > 35: 
  print(f"you are clinically obese")
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
counter = 0
if size == "S":
  counter += 15
  if add_pepperoni == "Y":
    counter += 2
    if extra_cheese == "Y":
      counter += 1
elif size == "M":
  counter += 20
  if add_pepperoni == "Y":
    counter += 2
    if extra_cheese == "Y":
      counter += 1
elif size == "L":
  counter += 25
  if add_pepperoni == "Y":
    counter += 2
    if extra_cheese == "Y":
      counter += 1
print(f"Your total comes to ${counter}")

