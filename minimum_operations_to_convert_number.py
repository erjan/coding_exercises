'''
You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:

If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:

x + nums[i]
x - nums[i]
x ^ nums[i] (bitwise-XOR)
Note that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.

Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.
'''


IDEA :
Go through all the possibilities.
we are storing each possibility in seen so Maximum space required is 1000.

'''

class Solution:
def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
    if start==goal:
        return 0
    
    q = [(start,0)]
    seen = {start}
    while q:
        n,s = q.pop(0)
        for num in nums:
            for cand in [n+num,n-num,n^num]:
                if cand==goal:
                    return s+1
                if 0<=cand<=1000 and cand not in seen:
                    seen.add(cand)
                    q.append((cand,s+1))
    
    return -1
    
------------------------------------------------------------------------------------------------

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = collections.deque([(start, 0)])
        visited = {start}
        
        while q:
            x, count = q.popleft()
            count += 1
            for num in nums:
                for newX in (x + num, x - num, x ^ num):
                    if newX == goal:
                        return count
                    if newX < 0 or 1000 < newX or newX in visited:
                        continue
                    visited.add(newX)
                    q.append((newX, count))
        
        return -1
