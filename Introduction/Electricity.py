unit = float(input("Enter the unit of electricity:"))

if unit <= 100:
    print("No charge")
elif unit <= 200:
    amount = (unit - 100) * 5
    print("Amount you have to pay is $", amount)
elif unit > 200:
    amount1 = ((unit - 200) * 10) + 500
    print("Amount you have to pay is $", amount1)
else:
    ("Enter a valid unit.")
