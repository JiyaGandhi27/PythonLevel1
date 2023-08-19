def reverse(A):
    reverse = 1
    for i in range(len(A)-1 , -1 , -1):
        reverse = A[i]
    return reverse
print(reverse([1,2,3,4,5,6,7]))