#### Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ''

ask_for_alpha = int(input('How many alphabetical characters would you like?\n'))

for char in range(1, ask_for_alpha + 1):
    get_alpha = random.choice(letters)
    password += get_alpha

ask_for_num = int(input('How many numbers would you like?\n'))

for num in range(1, ask_for_num + 1):
   get_num = random.choice(numbers)
   password += get_num


ask_for_special = int(input('How many special characters would you like to have?\n'))

for symbol in range(1, ask_for_special + 1):
    get_special = random.choice(symbols)
    password += get_special


print(password)    