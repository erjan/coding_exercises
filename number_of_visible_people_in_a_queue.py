'''
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.
'''

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0]*len(heights)
        stack = [] # mono-stack 
        for i in reversed(range(len(heights))): 
            while stack and stack[-1] <= heights[i]: 
                ans[i] += 1
                stack.pop()
            if stack: ans[i] += 1
            stack.append(heights[i])
        return ans 
      
-----------------------------------------------------------------------------
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        next_max = [-1 for i in range(len(heights))]
        res = [0 for i in range(len(heights))]
        for i in range(len(heights)-2, -1, -1):
            temp = i+1
            vis = 0
            while temp != -1:
                if heights[i] > heights[temp]:
                    vis += 1
                    temp = next_max[temp]
                else:
                    next_max[i] = temp
                    vis += 1
                    break
            res[i] = vis
        return res
