'''
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 
 '''

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        res = []
        for n in nums:

            s = str(n)
            for el in s:
                res.append(int(el))
        return res
      
--------------------------------------------------------------------------------------
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for item in nums:
            digit_list = list(map(int, str(item)))
            answer.extend(digit_list)
        return answer
      
-----------------------------------------------------------------------------------------------------
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(d) for n in nums for d in str(n)]
