'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        
        while l <= r:
            mid = (l + r) // 2
            if sum(math.ceil(num / mid) for num in nums) > threshold:
                l = mid + 1
            else:
                r = mid - 1
        return l
      
--------------------------------------------------------
def smallestDivisor(self, nums: List[int], threshold: int) -> int:
	def isValid(num):
		temp = 0
		for i in nums:
			temp += ceil(i/num)
		return temp <= threshold
	i, j = 1, max(nums) + 1   
	while(i <= j):
		mid = i + (j-i)//2
		if(isValid(mid)):
			j = mid-1
			ans = mid
		else:
			i = mid+1
	return ans
