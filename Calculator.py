## Print

print(""" _____________________
|  _________________  |
| |  Subtitlez +-*/ | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""", "\n" * 3 )


## Variables

num1 = int(input("Enter a number: "))
math = str(input("Enter a (+, *, /, -): "))
num2 = int(input("Enter another number: "))

def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "-":
        return number1 - number2

print(calculator(num1, num2, math))

replay = str(input("Do you wish to enter a new sum (Y/N)? ")).lower()

while replay == 'y':

    num1 = int(input("Enter a number: "))
    math = str(input("Enter a (+, *, /, -): "))
    num2 = int(input("Enter another number: "))

    print(calculator(num1, num2, math))

    replay = str(input("Do you wish to enter a new sum (Y/N)? ")).lower()

else:
    print('Bye!')
