alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(plain_text, shift_amount,Direction):
  cipher_text= ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if Direction == "encode":
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    else:
      new_position = position - shift_amount
      cipher_text += alphabet[new_position]
  print(f"the {Direction}d text is {cipher_text} ")
  


caeser(text,shift,direction)    

  