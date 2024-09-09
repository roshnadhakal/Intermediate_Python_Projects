# Password Generator using random, string modules
import random
import string

def generate_password(length):
    # Defining characters to include in the password: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters for the length specified by the user
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
print("Generated password:", generate_password(length))
