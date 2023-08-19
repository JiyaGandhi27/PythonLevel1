num = float(input("Enter any number:"))

if num%2==0 and num%3==0:
  print("The number is divisible by 2 and 3 both.")
elif num%2!=0 and num%3!=0:
  print("The number is not divisible by 2 and 3 both.")
elif num%2==0 and num%3!=0:
  print("Number is divisible by 2 but not by 3")
elif num%2!=0 and num%3==0:
  print("Number is divisible by 3 but not by 2")