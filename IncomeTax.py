
income = float(input('How much is your income? '))



if income >= 18001 and income <= 37000:
    print("$", income * 0.19)
elif income >= 37001 and income <= 90000:
    print('$', income * 0.3205)
elif income >= 90001 and income <= 180000:
    print("$", income * 0.37)
else:
    print("$", income * 0.45)

