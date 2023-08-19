rows = int(input("Enter any number:"))
for i in range(rows , 0 , -1):
  for j in range(i):
    print("*" , end = ' ')
  print("\n")