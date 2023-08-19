# Write a program to reverse a list.
#	B. You cannot use slicing
#	C. You cannot use an empty list
#	D. You cannot use the print statements inside any loop.

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

list2 = list
index3 = 1
index4 = 6

size2 = len(list2)

if((index3>=0 and index3<size) and (index4>=0 and index4<size2)):
  temp = list[index3]
  list[index3] = list[index4]
  list[index4] = temp
else:
  print("Enter valid indexes")

list3 = list2
index5 = 2
index6 = 5

size3 = len(list3)

if((index5>=0 and index5<size) and (index6>=0 and index6<size)):
  temp = list[index5]
  list[index5] = list[index6]
  list[index6] = temp
else:
  print("Enter valid indexes")

list4 = list3
index7 = 3
index8 = 4

size4 = len(list4)

if((index7>=0 and index7<size) and (index8>=0 and index8<size)):
  temp = list[index7]
  list[index7] = list[index8]
  list[index8] = temp
else:
  print("Enter valid indexes")

print("The updated list is:",list4)