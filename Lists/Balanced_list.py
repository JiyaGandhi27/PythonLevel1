#Consider a list = [1,2,4,5,2,3]
#The list is always going to have even number of elements.
#Find the integer that would be required to make the list balanced.
#To make the list balanced, find the sum of right and left halves.

A = [1,2,4,5,2,3]
l = len(A)
lefthalf = int(l / 2)
left_total = 0 
right_total = 0
for i in range (0 , lefthalf):
  left_total += A[i]
for j in range (lefthalf , l):
  right_total += A[i]
if right_total > left_total:
  print(right_total - left_total)
else:
  print(left_total - right_total)