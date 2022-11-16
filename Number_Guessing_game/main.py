import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

count = 0
is_game_over = False
guess = 0

def guess_game():
  global guess
  guess = int(input("Make a guess: ")) 
  if guess != number:
    if guess < number:
      print("Too low.") 
    elif guess > number:
      print("Too high.")
  elif guess == number:
    print(f"You got it! The answer was {number}.")

while not is_game_over == True:
  if not count == 1 or count == 9: 
    if diff_level == "easy":
      for _ in range(10):
        if guess == number:
          is_game_over = True
        else:
          count = 10 - _
          print(f"You have {count} attempts remaining to guess the number.")
          guess_game()
    else:
      for _ in range(5): 
        if guess == number:
          is_game_over = True
        else:
          count = 5 - _
          print(f"You have {count} attempts remaining to guess the number.")
          guess_game()
  else:
    if guess == number:
      is_game_over = True
    else:
      is_game_over = True
      print("You lose!")



  