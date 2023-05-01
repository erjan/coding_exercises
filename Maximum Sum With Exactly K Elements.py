'''
You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing the operation exactly k times.
'''


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        nums= [-n for n in nums]
        heapify(nums)
        ans = 0
        

        for i in range(k):

            temp = -heapq.heappop(nums)
            ans+= temp

            temp +=1
            heapq.heappush(nums,-temp)
        
        return ans

    
----------------------------------------------------------------------------------------------------------------------
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans = 0
        for _ in range(k):
            ans += max_num
            max_num += 1
        return ans
