'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []

        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)

        print(res)
        return res
      
--------------------------------------------------------------------
def rearrangeArray(self, nums: List[int]) -> List[int]: # nums = [3,1,-2,-5,2,-4]
        pos_arr = [num for num in nums if num > 0] # [3, 1, 2]
        neg_arr = [num for num in nums if num < 0] # [-2, -5, -4]
        output = list()
        for i in range(len(pos_arr)):
            output.append(pos_arr[i])
            output.append(neg_arr[i])
        return output # [3,-2,1,-5,2,-4]
