'''
Given an binary array nums and an integer k, 
return true if all 1's are at least k places away from each other, otherwise return false.
'''
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        temp = list()
        for i in range(len(nums)):

            if nums[i] == 1:
                temp.append(i)
        print(temp)
        for i in range(len(temp)-1):
            print('pair: ', temp[i], '\t', temp[i+1])
            if temp[i+1] - temp[i] <= k:
                print('bad')
                return False
        return True
