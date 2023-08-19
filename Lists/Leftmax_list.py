A = [-3,1,0,-1,2,6,4,8,4,3]
n = len(A)
LM = []
LM.append(A[0])
for i in range(1,n):
  if(LM[i-1]  > A[i]):
    LM.append(LM[i-1])
  else:
    LM.append(A[i])
print(LM)