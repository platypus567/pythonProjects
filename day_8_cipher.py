alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(plain_text, shift_amount):
  final_text = ""
  decrypted_text = ""
  if direction == "encode":
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      final_text += new_letter
    print(f"The encoded text is {final_text}")
  elif direction == "decode":
    for letter in text:
      position = alphabet.index(letter)
      new_position = position - shift_amt
      new_letter = alphabet[new_position]
      decrypted_text += new_letter
    print(f"The decrypted message is {decrypted_text}")
caesar(text, shift)
