import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&','*', '+', '@',]

print("Welcom to the PyPassword Generator!")
num_letters = int(input("How many letter would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

## Easy Level
# password = ""

# for char in range(1, num_letters +1):
#     password += random.choice(letters)

# for char in range(1, num_symbols +1):
#     password += random.choice(symbols)

# for char in range(1, num_numbers +1):
#     password += random.choice(numbers)

# print(password)

## Hard Level

password_list = []

for char in range(1, num_letters +1):
    password_list += random.choice(letters)

for char in range(1, num_symbols +1):
    password_list += random.choice(symbols)

for char in range(1, num_numbers +1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

hard_password = ""
for char in password_list:
    hard_password += char

print(f"Your password is: {hard_password}")