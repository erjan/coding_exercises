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
                
----------------------------
#stack based

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack = []
        
        for i in range(n):
            l = len(stack)
            if l == 0 or height[i] < height[stack[l - 1]]:
                stack.append(i)
            else:
                while(l > 0 and height[stack[l - 1]] <= height[i]):
                    ht = height[stack.pop()]
                    l = l - 1
                    ans = ans + (0 if l == 0 else (min(height[i],height[stack[l - 1]]) - ht) * (i - stack[l - 1] - 1))
                stack.append(i)
        return ans
                
        
