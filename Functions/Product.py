def product(A):
    product = 1
    for i in range (len(A)):
     product = product * A[i]
    return product
print(product([1,2,3,4,5,6,7]))

