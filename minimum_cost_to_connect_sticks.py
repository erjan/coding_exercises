'''
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

 

Example 1:

Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
Explanation: You start with sticks = [1,8,3,5].
1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
Example 3:

Input: sticks = [5]
Output: 0
Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.
'''

def leftpop_minimum(self, arr1, arr2):
    '''take 2 arrays and pop the minimum head'''

    if not arr1:
        return arr2.pop(0)
    if not arr2:
        return arr1.pop(0)
    if arr1[0] < arr2[0]:
        return arr1.pop(0)
    else:
        return arr2.pop(0)


def connectSticks(self, sticks):
    """
    :type sticks: List[int]
    :rtype: int
    """

    sticks.sort()
    cost, stack = 0, []

    while len(sticks) + len(stack) > 1:

        a = self.leftpop_minimum(sticks, stack)
        b = self.leftpop_minimum(sticks, stack)

        curr_cost = a+b
        cost += curr_cost
        stack.append(curr_cost)

    return cost
-------------------------------------------------------------------

import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            c = heapq.heappop(sticks)+heapq.heappop(sticks)
            res += c
            heapq.heappush(sticks,c)
        return res
----------------------------------------------------------------------------------

Explanation
We need to combine everything anyway, thus always sticks currently 2 smallest ones
Best data structure for this purpose is heap
Implementation
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n, heap = len(sticks), sticks
        heapq.heapify(heap)
        ans = 0
        for i in range(n-1):
            s = heapq.heappop(heap) + heapq.heappop(heap)
            heapq.heappush(heap, s)
            ans += s
        return ans 
A really cool feature of python heap is heapq.heapreplace. It's more efficient than heapq.heappop + heapq.heappush, below is an example

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n, heap = len(sticks), sticks
        heapq.heapify(heap)
        ans = 0
        for i in range(n-1):
            s = heapq.heappop(heap) + heap[0]
            heapq.heapreplace(heap, s)
            ans += s
        return ans 
---------------------------------------------------------------

import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        if len(sticks) < 2:
            return 0
        
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1: 
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            
            res += s1 + s2
            heapq.heappush(sticks, s1 + s2)
        
        return res
-----------------------------------------------------------------

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            ans += (s := heapq.heappop(sticks) + heapq.heappop(sticks))
            heapq.heappush(sticks, s)
        return ans    
-----------------------------------------------

from heapq import heappush,heappop,heapify
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        answer=[]
        while len(sticks)!=1:
            element=heappop(sticks)+heappop(sticks)
            heappush(sticks,element)
            answer.append(element)
        return sum(answer)
      
      
      
      
  
