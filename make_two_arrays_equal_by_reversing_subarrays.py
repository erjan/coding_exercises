'''
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.
'''


#DUMB SOLUTION - CHEATING..
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
    
    
#SOLUTION I LOOKED UP using dictionaries or collections counter

#this is just counting how many times each digit appears - another condition of equality
def f( target, arr):
    d1={}
    d2={}
    for i in target:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    print('d1 after filling')
    print(d1)
    
    for i in arr:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1

    print('d2 after filing')
    print(d2)
    return (d1==d2)

target = [1,2,3,4]
arr = [2,4,1,3]


f(target,arr)

#same with counter
from collections import Counter

def f( target, arr):
    c_target = Counter(target)
    c_arr = Counter(arr)
    
    result = c_target == c_arr
    print(result)

        
