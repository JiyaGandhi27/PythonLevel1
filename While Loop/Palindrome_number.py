num = int(input("Enter any number:"))
temp = num
rev = 0
digit = 0

while(num > 0):
  digit = num % 10
  rev = (rev*10) + digit
  num = num//10
print(rev)

if (temp == rev):
  print("It is a palindrome number")
else:
  print("It is not a palindrome number")
  