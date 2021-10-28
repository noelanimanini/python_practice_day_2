#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

# todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#  todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# print the list of words to show the user the randomized input with the press of a button

randomize = input(f"Welcome! Please press 'd' to randomize the word list, {word_list} ")

if randomize:
  ans = random.choice(word_list)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#todo-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(ans)

for letter in range(word_length):
  display.append("_")

guess = input("Guess a letter from a-z ").lower()


#todo-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
  letter = ans[position]
  if guess == letter:
    # given an array filled with dashes, I need to replace each dash at a specific index where that position matches the guess and the placement of the letter of that word. 
    display[position] = letter

print(display)

#todo-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3




