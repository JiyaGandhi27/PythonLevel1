income = float(input("Enter your income:"))

if income < 50000:
  tax = 0

elif income >=50000 and income < 100000:
  tax = 0.2*income

elif income >=100000:
  tax = 0.35*income

print("The overall tax to be pad by you is:", tax)