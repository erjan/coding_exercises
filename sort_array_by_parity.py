'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

#my own solution:
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = list(filter(lambda num: num %2 == 0, A))
        odds = list(filter(lambda num: num %2 == 1, A))
        
        return evens+ odds


# 2 pointer solution
import random, time
def f(a):
    low = 0
    high = len(a)-1
    print(a)
    while low < high:
        print('-----------------------')
        print(a)
        print()
        time.sleep(2)
        while a[low] %2 == 0 and low < high:
            time.sleep(3)
            print('even number found %d' % a[low])
            low+=1
        print('found odd instead of even! %d' % a[low])
        while a[high] %2 == 1 and low < high:
            time.sleep(3)
            print('odd number found  %d' % a[high])
            high-=1
        print('found even instead of odd! %d' % a[high])

        print('swapping %d %d'% (a[low], a[high]))
        a[low],a[high] = a[high], a[low]
        
    print()
    print(a)

res = []
for i in range(10):
    num = random.randint(1, 400)
    if num not in res:
        res.append(num)

f(res)
