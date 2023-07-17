import random

# Script intro message
print("********************************************************************")
print("* Generate a random password that consists of:                     *")
print("* Letters, Numbers, and Symbols.                                   *")
print("* When prompted enter how long you would like your password to be. *")
print("********************************************************************")
print("\n\n")

# ask user for length of password the want to create.
user_input_length = int(input("* Enter Desired Password Length:                                   *\n-->"))

# characters that contain letters, numbers, and symbols which will be used to generate password
characters_for_password="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# use random funtion to generate a random password for user.
# using the list of charachters generate a string of text based on length inputted by user
user_generated_password = "".join(random.sample(characters_for_password,user_input_length))

# print password that is generated for user
print("\n\n")
print("********************************************************************")
print("* Password has been generated:                                     *")
print("*------------------------------------------------------------------*")
print("-- '" +user_generated_password + "' --")
print("*------------------------------------------------------------------*")
print("********************************************************************")

