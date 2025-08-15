import random
import string

def generate_password(length=12):
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation

  all_chars = letters + digits + special_chars

  password = ''.join(random.choice(all_chars) for i in range(length))

  return password