'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
    
        if not height:
            return 0
        
        l = 0
        r = len(height)-1
        leftMax, rightMax = height[l], height[r]
        
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
                
                
        
