'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 
 '''

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
        res.reverse()
        return res
      
------------------------------------------
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # maintain monotonic decreasing stack
        # O(n) O(n)
        
        n = len(heights)
        stack = []
        for index in range(n):
            while stack and heights[stack[-1]] <= heights[index]:
                stack.pop()
            stack.append(index)
        return stack
--------------------------------------------

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = 0
        for idx in range(len(heights)-1,-1,-1):
            if heights[idx] > max_height:
                max_height = heights[idx]
                res.append(idx)
        
        return res[::-1]    
    #TC -> O(n) || SC -> O(1)
------------------------------------------

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        _max = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > _max:
                _max = heights[i]
                res.append(i)
        
        res.reverse()
        return res
-----------------------------------------

It looks like the Leetcode grader doesn't strictly require the return value to be a list as the type signature might imply. As such, we can return deques and arrays without having to convert them to a list first.

This solution is based on the one given in the "Solution" writeup with the following changes:

Pop items off the input height as we iterate to reduce memory usage
deque.appendleft() onto answers so we don't have to reverse the list before returning
Also on github at: https://github.com/catleeball/leetcode/blob/main/1762_Buildings_with_an_Ocean_View/solution.py

from typing import List, Deque
from collections import deque

# Runtime: 676 ms, faster than 89.05% of Python3 online submissions for Buildings With an Ocean View.
# Memory Usage: 27.9 MB, less than 99.92% of Python3 online submissions for Buildings With an Ocean View.
class Solution1:
    def findBuildings(self, heights: List[int]) -> Deque[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return deque([])
        if len(heights) == 1:
            return deque([0])

        answer: Deque[int] = deque()
        tallest: int = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings: int = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current: int = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.appendleft(index)
                tallest = current

        return answer
Very slightly smaller is using array instead of deque, which seems to use slightly less memory, but at the cost of a little more runtime (presumably due to the reverse operation at the end to make the order ascending).

from typing import List, Iterable
from array import array

# Runtime: 688 ms, faster than 79.26% of Python3 online submissions for Buildings With an Ocean View.
# Memory Usage: 27.3 MB, less than 99.98% of Python3 online submissions for Buildings With an Ocean View.
    def findBuildings(self, heights: List[int]) -> Iterable[int]:
        # Edge cases where we don't need to do anything.
        if not heights:
            return array('B')
        if len(heights) == 1:
            return array('B', [0])

        answer = array('I')
        tallest: int = 0
        # Required since pop from `heights` as we loop over it to reduce peak memory use.
        num_buildings: int = len(heights)

        # Note that we use a for loop instead of `while heights: heights.pop` so we can preserve indexes more easily.
        for index in reversed(range(num_buildings)):
            current: int = heights.pop()
            # If nothing taller to the right, it has an ocean view, append to answers list.
            if current > tallest:
                answer.append(index)
                tallest = current

        # Appending while we iterate backward over `heights` means it's currently in descending order.
        answer.reverse()
        return answer
----------------------------------------------------

Algo
Define a decreasing mono-stack which stores indices of height of decreasing order.

Implementation

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, x in enumerate(heights): 
            while stack and heights[stack[-1]] <= x: stack.pop()
            stack.append(i)
        return stack 
Analysis
Time complexity O(N)
Space complexity O(N)

A more straightforward approach would be scanning through the array in reverse order.

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        prev = 0
        for i in reversed(range(len(heights))):
            if prev < heights[i]: 
                ans.append(i)
                prev = heights[i]
        return ans[::-1]
      
      
      
    
