#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

# todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#  todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# print the list of words to show the user the randomized input with the press of a button

randomize = input(f"Welcome! Please press 'd' to randomize the word list, {word_list} ")

if randomize:
  ans = random.randint(1,len(word_list))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

guess = input("Guess a letter from a-z ")

guess.lower()

for choice in list(word_list[ans]):
  if guess == choice:
    print(guess == choice)
  else:
    print("youre wrong")




