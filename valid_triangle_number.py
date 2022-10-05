'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #a+c > b
        #a+b > c
        #b+c > a
        
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            a = nums[i]
            k = i +2
            for j in range(i+1, len(nums)):
                b = nums[j]
                
                while k < len(nums) and a + b > nums[k]:
                    k+=1
                if k > j:
                    res += k-j-1
                
        return (res)
      
-----------------------------------------------------------------------------------------
class Solution:
    def triangleNumber(self, T: List[int]) -> int:
    	L, t, _ = len(T), 0, T.sort()
    	for i in range(L-2):
    		k = i + 2
    		for j in range(i+1,L-1):
    			M = T[i] + T[j] - 1
    			if M < T[j]: continue
    			while k < L and T[k] <= M: k += 1
    			t += min(k, L) - (j + 1)
    	return t
		
    
----------------------------------------------------------

class Solution(object):
    '''
       As we know inorder to check if a triangle is valid or not, if its sides are given:=>
       A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is 
       greater than the third side. For Example, let A, B and C are three sides of a triangle. 
       Then, A + B > C, B + C > A and C + A > B.
       Following the same we can apply this in code... 
    '''
    def isValidTriangle(self,index,nums):
        l,r = 0, index-1
        ans  = 0
        while l < r:
            if nums[l] + nums[r] > nums[index]:
                ans += r - l
                r -= 1
            else:
                l += 1    
        return ans
    
    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0
        
        nums.sort()
        res = 0
        for i in range(2, len(nums)):
            res += self.isValidTriangle(i, nums) 
        
        return res
-----------------------------------------------------------------------------------------------------------------

#2 pointer approach

class Solution:
	def triangleNumber(self, nums: List[int]) -> int:
		res = 0
		nums.sort # O(nlogn)
		# Loop till (n-2) elements, coz we need to fix one number every time and deal with the other two!
		# O(n^2)
		for i in range(len(nums)-1, 1, -1): 
			fix = nums[i] # Fix a number
			strt = 0
			end = i-1
			# Deal with the other two numbers every time!
			while strt < end:
				if nums[strt]+nums[end] > fix:
					res += end-strt
					end -= 1
				else:
					strt += 1
		return res
      
