# ============================================
# PyPassword Generator
# --------------------------------------------
# A simple random password generator that lets
# the user decide how many letters, numbers, 
# and symbols to include. 
#
# Author: Manupriya Dhanush Vayalambron
# Language: Python
# ============================================

import random  # Importing random module for random selection

# Lists containing possible characters
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

# Taking user input for number of each type of character
num_letters = int(input("How many letters would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

# Empty list to collect all selected characters
pass_list = []

# Add random letters
for l in range(0, num_letters):
    pass_list.append(random.choice(letters))

# Add random numbers
for n in range(0, num_numbers):
    pass_list.append(random.choice(numbers))

# Add random symbols
for s in range(0, num_symbols):
    pass_list.append(random.choice(symbols))

# Shuffle the combined list to randomize character order
random.shuffle(pass_list)

# Convert list into a single string
password = ""
for i in pass_list:
    password += i

# Display the final password
print("Your password is:", password)
