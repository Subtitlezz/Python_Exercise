#### Tip Calculator

tip_percent = [10, 12, 15]

bill_total = float(input('What was the total of the bill?\n'))
tip_total = int(input('How much would you like to tip? 10, 12, or 15?\n'))
split_bill = int(input('How many people split the bill?\n'))


if tip_total == tip_percent[0]:
    ten_tip = bill_total * 0.10
    total = (ten_tip + bill_total) / split_bill
    print(f'each person should pay: {total}')
elif tip_total == tip_percent[1]:
    twelve_tip = bill_total * 0.12
    total = (twelve_tip + bill_total) / split_bill
    print(f'each person should pay: {"{:.2f}".format(total)}')
elif tip_total == tip_percent[2]:
    fifteen_tip = bill_total * 0.15
    total = (fifteen_tip + bill_total) / split_bill
    print(f'each person should pay: {total}')
