import re
from art import logo
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ''
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    indexOfAlpha = alphabet.index(letter)
    indexOfAlpha += shift_amount
    end_text += alphabet[indexOfAlpha]
  print(f"The {direction}d text is {end_text}")


runAgain = True
while runAgain:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  should_continue = input("Type 'Yes' if you want to go again. otherwise type 'No':\n ").lower()
  if should_continue == "no":
    runAgain = False
    print("Goodbye!")

