A = [1,1,0,0,1,0,0,1,1,0,1,0,1]
size = len(A)
l = 0
r = size-1

while (l <= r):
  if(A[l] == 0):
    l+=1
  elif(A[r] == 0):
     r-=1
  else:
    A[l],A[r] = A[r],A[l]
print(A)