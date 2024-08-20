average_age = 90
weeks_in_year = 52

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a whole number.")
    age = int(input("Enter your age: "))

calculation = print((average_age - age) * weeks_in_year)
