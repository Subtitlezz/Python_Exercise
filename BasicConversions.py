## Conversion Program to convert lengths and weights

## Length Conversions
centimetre = 0.393 ## inches
metre = 3.281 ## feet
kilometre = 0.621 ## miles
inch = 2.54 ## centimetres
foot = 0.305 ## meters
mile = 1.609 ## Kilometres

## Weight conversions
gram = 0.035 ## ounces
kilogram = 2.204 ## pounds
ounce = 28.35 ## grams
pound = 0.454 ## kilograms

## Volume
millilitre = 0.035 ## fluid ounces
litre = 0.878 ## quarts
fluid_ounce = 28.413 ## millilitres
quart = 1.137 ## litres

ask_type = str(input('What would you like to convert from?: '))
ask_float = float(input('Conversion amount: '))

if ask_type == 'centimetre':
    print(ask_float / centimetre, 'inches')
elif ask_type == 'metre':
    print(ask_float / metre, 'feet')
elif ask_type == 'kilogram':
    print(ask_float / kilogram, 'miles')
elif ask_type == 'inch':
    print(ask_float / inch, 'centimetre')
elif ask_type == 'foot':
    print(ask_float / foot, 'meters')
elif ask_type == 'mile':
    print(ask_float / mile, 'kilometers')
elif ask_type == 'gram':
    print(ask_float / gram, 'ounces')
elif ask_type == 'kilogram':
    print(ask_float / kilogram, 'pounds')
elif ask_type == 'ounce':
    print(ask_float / ounce, 'grams')
elif ask_type == 'pound':
    print(ask_float / pound, 'kilograms')
elif ask_type == 'millilitre':
    print(ask_float / millilitre, 'fluid ounces')
elif ask_type == 'litre':
    print(ask_float / litre, 'quarts')
elif ask_type == 'fluid_ounce':
    print(ask_float / fluid_ounce, 'millilitres')
elif ask_type == 'quart':
    print(ask_float / quart, 'litres')
else:
    print('Not convertable')









