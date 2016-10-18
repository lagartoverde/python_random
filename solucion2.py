'''
Created on 26 de sept. de 2016

@author: lagarto
'''
import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors
x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print (x)
        break
tt = time()-t
print (tt)