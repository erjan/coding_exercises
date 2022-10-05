'''
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.
'''

  def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def helper(val):
			# sum = (start + end) * len //2
            if val > index:
                l = (val-1 + val-index) * index // 2
            else:
                l = (val-1 + 1) * (val -1) // 2 + (index - val + 1) # remain part we assign 1 to get minimum sum
            if val > n - 1 - index:
                r = (val-1+val - n + 1 + index) * (n -1 - index) // 2
            else:
                r = (val-1+1) *(val-1) //2 + (n-1-index - val +1) # remain part we assign 1 to get minimum sum
            return l + r > maxSum - val
            
        left, right = 1, maxSum - n + 1
        while left < right:
            mid = (left+right)//2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left if not helper(left) else left - 1
      
-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxValue(self, n: int, i: int, maxSum: int) -> int:
        """
         0  ...    i  ...    n
        [1, .... , x, .... , 1]
        
        So Here we have to find value at index i which should be maximized,
        such that total sum of array should be less than or Equal to maxSum
        
        Also said that array should only contain positive numbers...ie... not even zeros
        
        So Here we will maxmize x and add sum of leftSide and sum of rightSide
        x + leftSIde + RightSide
        
        Array will be like a mountain,
                        i
        [1, .... , x-1, x, x-1, .... , 1]
        
        no of Elements on leftSide --> i
        no of Elements on RightSide --> n - i - 1
        """
        start, end = 1, maxSum # maxValue possible at index is in range [1, maxSum]
        res = 0
        while (start <=  end):
            mid = start + (end - start) // 2
            
            eleOnLeft = min(i, mid - 1) 
            leftSum = self.sum(eleOnLeft, mid - 1)
            leftSum += max(0, i - mid + 1) # Adding the remaining 1's to the leftSum
            
            eleOnRight = min(n - i - 1, mid - 1)
            rightSum = self.sum(eleOnRight, mid - 1)
            rightSum += max(0, n - i - 1 - mid + 1) # Adding the remaining 1's to the RightSum
            
            if mid + leftSum + rightSum <= maxSum:
                res = max(res, mid)
                start = mid + 1
            else:
                end = mid - 1
                
        return res
    
    def sum(self, ele, x):
        """
        sum of range [1, n] --> n * (n + 1) // 2
        
        sum of range [x, n] --> (n * (n + 1) // 2) - (x * (x + 1) // 2)
        
        """
        totalSum = x * (x + 1) // 2
        rem = x - ele
        partialSum = rem * (rem + 1) // 2
        
		return totalSum - partialSum
