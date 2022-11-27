'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
'''


-----------------------------------------------------------------
class Solution:
    def pivotInteger(self, n: int) -> int:

        pref = [1]
        if n == 1:
            return 1
        a = [i for i in range(1, n+1)]
        for i in range(2, n+1):
            pref.append(pref[-1]+i)



        for i in range(len(pref)):

            if pref[i] == pref[-1] - pref[i-1]:
                print('found! at %d' % pref[i])
                print('at index i %d ' % (i+1))
                return i+1
        print('bad!')
        print('-1')
        return -1
      
-------------------------------------------------------

class Solution:
    def pivotInteger(self, n: int) -> int:
        s = sum([i for i in range(1, n + 1)])
        curSum = 0
        for i in range(1, n + 1):
            curSum += i
            if curSum == s - curSum + i:
                return i
        return -1
      
