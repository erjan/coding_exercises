'''
A sequence of numbers is called arithmetic if 
it consists of at least two elements, and the 
difference between every two consecutive elements 
is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
'''


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def getdiff(arr):

            temp = set()
            for i in range(len(arr)-1):
                temp.add(arr[i+1] - arr[i])
            return len(temp) < 2

        res = list()
        for i, j in list(zip(l, r)):
            sub = nums[i:(j+1)]

            sub.sort()
            if getdiff(sub):
                res.append(True)
            else:
                res.append(False)

        print(res)
        return res
