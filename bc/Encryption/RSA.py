import math
import random


def millerRabin(n, d):
    
    a = 2 + random.randint(1, n-4)
    
    x = pow(a, d, n)
    
    if x == 1 or x == n-1:
        return True
    
    while d != n-1:
        x = (x*x)%n
        d *= 2
        
        if x == 1:
            return False
        if x == n-1:
            return True
        
    return False


def isPrime(n, k):
    
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n-1
    while d % 2 == 0:
        d //= 2
    
    for i in range(0, k):
        if millerRabin(n, d) == False:
            return False
    
    return True


def generateKey(len):
    if len <= 4:
        print("Key of length less than 4 can't be created...")
        return
    
    lowerBound = 2 << (len-1)
    upperBound = 2 << (len)

    p, q = -1, -1
    
    while p == -1:
        randNum = random.randint(lowerBound+1, upperBound-1)
        if isPrime(randNum, 10):
            p = randNum
    while q == -1:
        randNum = random.randint(lowerBound+1, upperBound-1)
        if isPrime(randNum, 10) and randNum != p:
            q = randNum
    
    print(p, q)

generateKey(10)