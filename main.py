#alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(plain_text, shift_amount,Direction):
  
  cipher_text= ""
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
      if Direction == "encode":
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      else:
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    else:
      cipher_text+=char    
    
   
  print(f"the {Direction}d text is {cipher_text} ")


  
from art import logo
print(logo)
Game_on = True

while Game_on == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caeser(text,shift,direction)    

  result = input ("Do you want to play again?: YES OR NO?\n")
  if result == "YES" or "yes":
    Game_on = True
  else:
    Game_on = False


  