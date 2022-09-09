'''
Given a list of integer nums, return the earliest index i such that the sum of the numbers left of i is equal to the sum of numbers right of i. If there's no solution, return -1.

Sum of an empty list is defined to be 0.
'''

class Solution:
    def solve(self, nums):
        r = sum(nums)
        l = 0
        for i,x in enumerate(nums):
            r -= x
            if r == l:
                return i
            l += x
        return -1
---------------------------------------
#wrong solution


def solve(nums):

    pref = []
    pref.append(nums[0])
    for i in range(1, len(nums)):
        pref.append(nums[i] + pref[i-1])

    print('array')
    print(nums)
    print()
    print('pref is')
    pref.insert(0, 0)
    print(pref)

    # suffix
    n = len(nums)
    suf = [0 for _ in range(n)]
    suf[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        suf[i] = suf[i+1] + nums[i]

    print()
    suf.append(0)
    print('suf')
    suf = sorted(suf, reverse=False)
    print(suf)

    for i in range(len(pref)):
        if pref[i] == suf[i]:
            return i
    return -1
