import random
from hangman_art import logo, stages
from hanman_words import chosen_word

#hangman logo
print(logo)

#Choosing random Word
Rand_word = random.choice(chosen_word)

print(f"The Solution is {Rand_word}")

#Create blanks
display = []

for _ in range(len(Rand_word)):
  display += '_'
a = 0
lives = 6
end_of_game = False

while not end_of_game:
  guess = input("Guess a Letter: ").lower()
  print("---------------------")
  print(stages[lives])
  
  
  #If the user has entered a letter they've already guessed.
  if guess in display:
    print(f"You've already guessed {guess}")

  #Check guessed letter
  for position in range(len(Rand_word)):
    letter = Rand_word[position]
    if letter == guess:
      display[position] = letter
  
  #Check if user is wrong.
  if not guess in Rand_word:

    #it's not in the word.
    print(f"You guessed {guess}, that is not in the word. You lose a life!")

    if not lives == 0:
      lives -= 1
    else:
      end_of_game = True
      print("You Lose")
  
  #Check if user has got all letters.    
  elif "_" not in display:
    end_of_game = True
    print("You Win")
