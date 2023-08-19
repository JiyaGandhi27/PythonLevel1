# Write a program to swap the first and last elements of a list

index1 = 0
index2 = 7

list = [1,36,54,48,29,0,67,42]

size = len(list)

if((index1>=0 and index1<size) and (index2>=0 and index2<size)):
  temp = list[index1]
  list[index1] = list[index2]
  list[index2] = temp
else:
  print("Enter valid indexes")

print("The updated list is:",list)