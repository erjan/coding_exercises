'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = nums
        a.sort()
        count = 0
        res = []
        for i in range(len(a)-1):
            if a[count] == a[count+1]:
                res.append(a[count])
            count+=1
        return res
