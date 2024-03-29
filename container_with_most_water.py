'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # length of input array
        size = len(height)
        
        # two pointers, left init as 0, right init as size-1
        left, right = 0, size-1
        
        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1
        
        # area also known as the amount of water
        area = 0
        
		# trade-off between width and height
        # scan each possible width and compute maximal area
        for width in range(max_width, 0, -1):
            
            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left] )
                
                # update left index to righthand side
                left += 1
                
            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right] )
                
                # update right index to lefthand side
                right -= 1
                
        return area
