# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_int = float(height)
weight_int = float(weight)
bmi = weight_int / (height_int * height_int)
bmi_round = int(bmi)
print(bmi_round)
