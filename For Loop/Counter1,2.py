counter1 = int(input("Enter any number:"))
counter2 = int(input("Enter any number:"))
for i in range(1,counter1):
  if i%2==0:
    print(i+1)
for i in range(1,counter2):
  if i%2!=0:
    print(i+3)