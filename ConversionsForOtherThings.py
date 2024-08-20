
## Temperature Conversion

print('1. Temp, 2. Geometry, 3. Nutrion, 4. Finance')

ask_conversion_type = str(input('What would you like to convert?')).lower()

if ask_conversion_type == '1' or ask_conversion_type == 'temp':
    ask_for_temp_type = str(input("Enter a temperature type you are converting (C/F)?: ")).lower()

    if ask_for_temp_type == "c" or ask_for_temp_type == "celsius":
        celsius = float(input("Enter a temperature in Celsius: "))
        print(celsius * 9 / 5 + 32, 'Farenheit')

    elif ask_for_temp_type == "f" or ask_for_temp_type == "fahrenheit":
        fahrenheit  = float(input("Enter a temperature in Fahrenheit : "))
        print((fahrenheit  - 32) * 5 / 9, 'Celsius')

## Geometry Convertor
if ask_conversion_type == '2' or ask_conversion_type == 'geometry':
    ask_for_geo = str(input("1. \"Area\" of a circle\n2. \"Circumference\" of a Circle\nPick which one: ")).lower()
    if ask_for_geo =='1' or ask_for_geo =='area':
        area = float(input("Enter a area of circle: "))
        print(2 * 3.1416 * area, 'is the circumference of a circle')
    elif ask_for_geo =='2' or ask_for_geo =='circumference':
        circumference = float(input("Enter a circumference of circle: "))
        print(3.1416 ** circumference, 'is the radius of circle')

## BMI Calculator

if ask_conversion_type == '3' or ask_conversion_type == 'nutrion':
    ask_for_weight = str(input("Enter a weight in kilograms: ")).lower()
    ask_for_height = float(input("Enter a height in meters: "))
    print(ask_for_weight / (ask_for_height * ask_for_height), 'is your BMI')

## Interest Rate Calculator

if ask_conversion_type == '4' or ask_conversion_type == 'finance':

    amount_given = float(input("Enter the amount loaned to you $: "))
    interest = float(input("Enter the interest rate: "))
    loan_time = float(input("Enter the payback loan time in years: "))
    print(amount_given * (interest / 100) * loan_time, "You will accure this much interest")







