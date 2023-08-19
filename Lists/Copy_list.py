# Write a program to copy all the elements of a list to a new list.

list = [47 , 8 ,30 , 29 , 76 , 58 , 93 , 11]

new_list = []

for i in range(len(list)):
  new_list.append(list[i])
print(new_list)