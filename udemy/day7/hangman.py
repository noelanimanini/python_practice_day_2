#Step 1 
import random
import hangman_words as words 
import hangman_art as art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = words.word_list
print(art.logo)
randomize = input(f"Welcome! Please press 'd' to randomize the word list, {word_list} ")

if randomize:
  ans = random.choice(word_list)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#todo-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(ans)
lives = 6 


for letter in range(word_length):
  display.append("_")

end_of_game = False

while not end_of_game: 
  guess = input("Guess a letter from a-z ").lower()
  #todo-2: - Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

  for position in range(word_length):
    letter = ans[position]
    if guess == letter:
      display[position] = letter

  if guess != letter:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose")
  print(f"{' '.join(display)}")

  if "_" not in display:
    print("You Won!")

#todo-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3
  print(stages[lives])



