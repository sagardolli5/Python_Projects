import random
import os
from art import logo

def clear():
  os.system('cls')
  
def random_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)  

def play_game(): 
  print(logo)
  user_card = []
  computer_card = []
  is_game_over= False
  
  for _ in range(2):
    user_card.append(random_card())
    computer_card.append(random_card())
  
  while not is_game_over:
    user_score = calculate_score(user_card)
    compute_score = calculate_score(computer_card)
  
    print(f"   Your Cards: {user_card}, Current Score: {user_score}")
    print(f"   Computer's First Card: {computer_card[0]}")
    
    if user_score == 0 or compute_score == 0 or user_score > 21:
      is_game_over = True
    else:
      play_forAnotherCard = input("Type 'y' to get another card, type 'n' to pass:").lower()
      if play_forAnotherCard == "y":
        user_card.append(random_card())
      else:
        is_game_over = True
        
  while compute_score != 0 and compute_score < 17:
    computer_card.append(random_card())
    compute_score = calculate_score(computer_card)
    
  def compare(user, computer):
    if user == computer:
      print("It's Draw!")
    elif computer == 0:
      print("Lose, opponent has Blackjack")
    elif user_score == 0:
      print("Win with a Blackjack")
    elif user_score > 21:
      print("You went over. You lose")
    elif compute_score > 21:
      print("Opponent went over. You win")
    elif user > computer:
      print("You win")
    else:
      print("You lose")
  print(f"   Your final hand:{user_card}, final score: {user_score}")
  print(f"   Computer's final hand:{computer_card}, final score: {compute_score}")
  
  compare(user_score, compute_score)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()
