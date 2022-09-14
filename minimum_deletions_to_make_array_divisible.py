'''
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

Note that an integer x divides y if y % x == 0.
'''

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        nums.sort()
        x = reduce(gcd, numsDivide)
        
        count = 0
        for num in nums:
            if x%num == 0:
                return count
            count+=1
        return -1     
-----------------------------------------------------------------------------------------------------
class Solution:
                    # From number theory, we know that an integer num divides each
                    # integer in a list if and only if num divides the list's gcd.
                    # 
                    # Our plan here is to:
                    #   • find the gcd of numDivide
                    #   • heapify(nums) and count the popped elements that do not
                    #     divide the gcd.
                    #   • return that count when and if a popped element eventually
                    #     divides the gcd. If that never happens, return -1 
        
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
	
        g, ans = gcd(*numsDivide), 0            # <-- find gcd (using * operator)

        heapify(nums)                           # <-- create heap

        while nums:                             # <-- pop and count

            if not g%heappop(nums): return ans  # <-- found a divisor? return count
            else: ans+= 1                       # <-- if not, increment the count

        return -1                               # <-- no divisors found
		
#--------------------------------------------------
class Solution:    # version w/o heap. Seems to run slower
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
	
        g = gcd(*numsDivide)
        nums.sort()

        for i,num in enumerate(nums):
            if not g%num: return i

        return -1
