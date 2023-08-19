import math

def isPrime (n):
    count = 0
    for i in range(1,(int)(math.sqrt(n))+1):
        if(n % i == 0 ):
            if(i*i == n):
                count = count + 1
            else:
                count = count + 2
    print(count)
    if (count == 2):
        return True
    else:
        return False
    
num = 100
print(isPrime(num))