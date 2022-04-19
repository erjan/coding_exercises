'''
You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can be pushed into the warehouse from either side (left or right)
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.
'''

Algo
First, compute the actual height that a room in warehouse can provide. Then, check the rooms from lowest to highest to accommodate a box as small as possible.

Implementation

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ans = lo = 0
        hi = len(warehouse)-1
        for box in sorted(boxes, reverse=True): 
            if lo <= hi: 
                if box <= warehouse[lo]: 
                    lo += 1
                    ans += 1
                elif box <= warehouse[hi]: 
                    hi -= 1
                    ans += 1
        return ans
Analysis
Time complexity O(MlogM + N)
Space complexity O(M)

1564. Put Boxes Into the Warehouse I
1580. Put Boxes Into the Warehouse II

My original solution is longer than necessary.

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        ht = [0]*len(warehouse) # accessible height 
        prefix = suffix = inf 
        for i in range(len(warehouse)):
            ht[i] = max(ht[i], prefix := min(prefix, warehouse[i]))
            ht[~i] = max(ht[~i], suffix := min(suffix, warehouse[~i]))
        
        ans = i = 0 
        boxes.sort()
        for h in sorted(ht): 
            if i < len(boxes) and boxes[i] <= h: 
                ans += 1
                i += 1
        return ans 
      ---------------------------------------------------------------------
      The key is to observe that if we have warehouse [4,5,4], then we never get a chance to add a box to the middle one. From this we can also observe that the valid height in the middle should always be the maximum of left boundary and right boundary. This gives the algorithm

start from left and right and calculate the boundary height for each room in the warehouse
start from the smallest box and add each one in until we cannot add anymore or we add all of them in.
code

def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        if not warehouse: return 0
        l,r = 0,len(warehouse)-1
        stack = []
        min_l,min_r = sys.maxsize,sys.maxsize
        while l<= r:
            min_l = min(min_l,warehouse[l])
            min_r = min(min_r,warehouse[r])
            if min_l >= min_r:
                stack.append(min_l)
                l+=1
            else:
                stack.append(min_r)
                r-=1

        asr = 0
        boxes.sort(reverse = True)
        while boxes:
            while stack and stack[-1] < boxes[-1]:
                stack.pop()
            if not stack: return asr
            stack.pop()
            boxes.pop()
            asr+=1
        return asr
--------------------------------------------------------------------------
The idea is to put biggest box at a time to either leftmost or rightmost place, and return how many places have we filled in the warehouse.

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        box_id, left, right = 0, 0, len(warehouse)-1
        while left <= right and box_id < len(boxes):
            if boxes[box_id] <= warehouse[left]:
                left += 1
            elif boxes[box_id] <= warehouse[right]:
                right -= 1
            box_id += 1
        return left + (len(warehouse)-1-right)
------------------------------------------------------------------------------------
Explanation
Key Idea: since we can push boxes from both sides, the maximum box height we can push to warehouse i is decided by max(min(rooms_on_the_left_side_of_i), min(rooms_on_the_right_side_of_i))
Then we do 2 for loops to find out the current maximum based on above logic
One loop from left to right, get the minimum
The other loop from right to left, get the minimum
Then sort height and boxes reversely (large to small)
Using two pointer & greedy, we can easily find out how many boxes can fit
Greedly, if a box can fit in warehouse, we count it as fit, then move on to the next box and room
Otherwise, move to next box (smaller than before) and check if it will fit the current room
Implementation
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        height, cur_min = [], sys.maxsize
        for room in warehouse:
            cur_min = min(cur_min, room)
            height.append(cur_min)
        cur_min, n = sys.maxsize, len(warehouse)
        for i, room in enumerate(warehouse[::-1]):
            cur_min = min(cur_min, room)
            height[n-1-i] = max(height[n-1-i], cur_min)
            
        height.sort(reverse=True)    
        boxes.sort(reverse=True)
        m, i, j, ans = len(boxes), 0, 0, 0
        while i < m and j < n:
            if height[j] >= boxes[i]: i, j, ans = i+1, j+1, ans+1
            else: i += 1
        return ans
      
      
      
