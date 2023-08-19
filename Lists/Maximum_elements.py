# Write a program to find the maximum element in a list.

list = [1, 36, 54, 48, 29, 0, 67, 42]

max = list[0]

for i in range (len(list)):
  if max < list[i]:
    max = list[i]
print(max)