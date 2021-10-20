import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

question = input("what is your choice? type 0 for ROCK, 1 for PAPER and 2 for SCISSORS\n")
answers = [rock, paper, scissors]

if question == 0:
  print(rock)
  print("rock")
  result = random.randint(0, len(answers))
  if result == 0:
    print(rock)
    print("rock")
    print("try again! ")
  elif result == 1:
    print(paper)
    print("paper")
    print("you lose! ")
  else: 
    print(scissors)
    print("scissors")
    print("you win! ")
elif question == 1:
  print(paper)
  print("paper")
  result = random.randint(0, len(answers))
  if result == 0:
    print(rock)
    print("rock")
    print("you win! ")
  elif result == 1:
    print(paper)
    print("paper")
    print("try again! ")
  else: 
    print(scissors)
    print("scissors")
    print("you lose! ")
else: 
  print(scissors)
  print("scissors")
  result = random.randint(0, len(answers))
  if result == 0:
    print(rock)
    print("rock")
    print("you lose! ")
  elif result == 1:
    print(paper)
    print("paper")
    print("you win! ")
  else: 
    print(scissors)
    print("scissors")
    print("try again! ")
  
