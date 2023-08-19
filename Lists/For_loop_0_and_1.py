A = [1,1,0,0,1,0,0,1,1,0,1,0,1]

l = len(A)

for i in range (0 , l):
  for j in range(i , l):   
    if(A[i] > A[j]):
      temp = A[i]
      A[i] = A[j]
      A[j] = temp
print(A)