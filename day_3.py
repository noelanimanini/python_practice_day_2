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
