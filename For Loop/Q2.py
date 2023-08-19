n = int(input("Enter any number:"))

sum = 0

for i in range(1, n+1):
  avg = (sum + i)/n

print("The average of first", n , "natural numbers is", avg)