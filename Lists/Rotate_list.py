A = [1,9,8,2,3,-1,41,82,4]
B = 2
n = len(A)

#reversing a list
start = 0
end = n-1
while(start < end):
  A[start], A[end] = A[end], A[start]
  start += 1
  end -= 1
print(A)

#reversing the first B elements
start = 0
end = B-1
while(start < end):
  A[start], A[end] = A[end], A[start]
  start += 1
  end -= 1
print(A)

#reversing the remaining N-B elements
start = B
end = n-1

while(start<end):
  A[start], A[end] = A[end], A[start]
  start += 1
  end -= 1
print(A)