# Write a program to find the minimum element in a list.

list = [1, 36, 54, 48, 29, 0, 67, 42]

min = list[0]

for i in range (len(list)):
  if min > list[i]:
    min = list[i]
print(min)