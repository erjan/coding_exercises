'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the 
numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 '''

#my own solution!!!!!!!
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    
        actual_set = [i for i in range(1, len(nums)+1)]
    
        d = dict()

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        repeating = 0
        for k, v in d.items():
            if v > 1:
                repeating = k
                break
      
        missing_num = 0
        for i in range(len(actual_set)):
            if actual_set[i] not in nums:
                missing_num = actual_set[i]
     
        del nums
        del actual_set
        del d
        return [repeating, missing_num]

