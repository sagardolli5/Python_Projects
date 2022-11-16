import os
from art import logo

def clear():
  os.system('cls')

print(logo)
print("Welcome to the secret auction program.")


bidders ={}
auction_run = True
while auction_run:
    name=input("What is your name? : ").lower()
    amount=int(input("What is your bid? : $"))
    other_bidders = input("Are there any bidders? type 'Yes' or 'No'.: \n").lower()
    bidders[name] = amount
    if other_bidders == "yes":
      auction_run = True
      clear()
    else:
      auction_run = False

max_value = 0
for person in bidders:
  if bidders[person] > max_value:
    max_value = bidders[person]
    max_value_name = person
print(f"The winner is {max_value_name} with a bid of ${max_value}")