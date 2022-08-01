'''
Даны 2 целых числа n и m. Написать функцию gcd, которая возвращает наибольший общий делитель (НОД) этих двух чисел.
'''

import math

class Answer:
    def gcd(self, a, b): 
        
        return math.gcd(a,b)
        
---------------------------------------
#EUCLIDEAN ALGO
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
   
------------------------------------------------
#using loops
def gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
