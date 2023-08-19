# Write a program to count the frequency(the number of times the element is appearing in a list) of a specific element in a list.

list = [1 , 57 , 4 , 1 , 90 , 67 , 57 , 1 , 4 , 2 , 90 , 1 , 57 , 4 , 2 , 1]

count = 0

num = int(input("Enter a number to know its frequency:"))

for i in range (len(list)):
  if num == list[i]:
    count +=1
print(count)