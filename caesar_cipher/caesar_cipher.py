# Create an encrypt function that takes in a plain text phrase and a numeric shift.
#   The phrase will then be shifted that many letters

def encrypt(plain, key):
  # plain: abcdef
  # key: 2
  # -> 'cdefgh'
  
  encrypted_text = ''

  for character in plain:
    print(f'plain character of {character} not yet shifted by {key}')
    encrypted_character = character
    encrypted_character += 2
    print(f'encrypted character of {character} shifted by {key}')

  # shift the plain text
  # store the shifted value
  # return the shifted value





if __name__ == "__main__":
  encrypt('abcdef', 2)





# Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

# reverses the key in opposite direction of encrypt function
def decrypt(encrypt, key):
  return encrypt(encrypted, -key)

# Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.





# Devise a method for the computer to determine if code was broken with minimal human guidance.