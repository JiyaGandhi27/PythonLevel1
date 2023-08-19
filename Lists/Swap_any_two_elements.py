# Write a program to swap any two elements of a list. Take the value of indexes to be swapped from the user. Check if the indexes are valid or not. If valid, then swap the elements else do not swap.

index1 = int(input("Enter the first index:"))
index2 = int(input("Enter the second index:"))

list = [1,36,54,48,29,0,67,42]
#      [42,67,0,29,48,54,36,1]
size = len(list)

if((index1>=0 and index1<size) and (index2>=0 and index2<size)):
  temp = list[index1]
  list[index1] = list[index2]
  list[index2] = temp
else:
  print("Enter valid indexes")

print("The updated list is:",list)