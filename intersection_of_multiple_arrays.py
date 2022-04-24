
'''
Given a 2D integer array nums 
where nums[i] is a non-empty array of distinct positive integers, return 
the list of integers that are present in each array of nums sorted in ascending order.
 
 '''

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        total = len(nums)
        print('total', total)
        temp = list()
        for n in nums:
            temp.extend(n)

        temp = dict(Counter(temp))
        print(temp)
        res = []
        for k in temp.keys():
            if temp[k] == total:
                res.append(k)
        res.sort()
        print('result', res)
        return res
