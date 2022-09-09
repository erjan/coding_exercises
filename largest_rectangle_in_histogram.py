'''
Given an array of integers heights representing
the histogram's bar height where the width of each bar is 1, return the
area of the largest rectangle in the histogram.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair of el (index,height)
        
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea, height*(i-index)) # width = i - index
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea
        
