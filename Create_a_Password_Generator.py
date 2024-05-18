import string
import random

# Define characters for the password
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&','*', '+', '@',]

print("Welcome to the PyPassword Generator!")

while True:
    try:
        # Get the number of each type of character for the password
        num_letters = int(input("How many letter would you like in your password?\n"))
        num_symbols = int(input("How many symbols would you like in your password?\n"))
        num_numbers = int(input("How many numbers would you like in your password?\n"))
    
        # Generate the password list
        password_list = []
        
        for char in range(1, num_letters +1):
            password_list += random.choice(letters)
        
        for char in range(1, num_symbols +1):
            password_list += random.choice(symbols)
        
        for char in range(1, num_numbers +1):
            password_list += random.choice(numbers)
        
        # Shuffle the password list to ensure randomness
        random.shuffle(password_list)
        
        # Join the list to form the final password string
        hard_password = ''.join(password_list)
        
        # Display the result
        print(f"Your password is: {hard_password}")
        break
    
    except ValueError:
        print("Error: Please enter a numeric value")