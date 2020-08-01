'''
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
'''


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a = arr
        a = sorted(a)
        diff = a[1]-a[0]
        for i in range(1,len(a)):
            if a[i] - a[i-1] != diff:

                #print('bad.. ! %d - %d ' %(a[i], a[i-1]))
                return False
        return True
