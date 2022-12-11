'''
You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.

A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.

The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.

More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.
The cost of a path is the maximum length of a jump among all jumps in the path.

Return the minimum cost of a path for the frog.
'''

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        vis = [False for i in range(n)]
        fwd = 0
        ans = -math.inf
        for i in range(0,n-1,2):
            vis[i] = True
            ans = max(ans,stones[i] - fwd)
            fwd = stones[i]
        ans = max(ans,stones[-1] - fwd)
        bwd = stones[-1]
        for i in range(n-1,0,-1):
            if not vis[i]:
                vis[i] = True
                ans = max(ans,bwd - stones[i])
                bwd = stones[i]
        ans = max(ans,bwd - stones[0])
        return ans
            
-----------------------------------------------------------------------------------------------
from collections import deque
import math

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n, _max = len(stones),  -math.inf
        
        dq1, dq2 = deque([0]), deque([0])
        for i in range(1,n-1):
            if i % 2 == 0:
                dq1.append(stones[i])
            else:    
                dq2.append(stones[i])

        dq1.append(stones[n-1])
        dq2.append(stones[n-1])
        dq_prev = dq1.popleft()
        while dq1:    
            dq_curr = dq1.popleft()
            _max = max(_max, abs(dq_curr-dq_prev))
            dq_prev = dq_curr

        dq_prev = dq2.popleft()
        while dq2:    
            dq_curr = dq2.popleft()
            _max = max(_max, abs(dq_curr-dq_prev))
            dq_prev = dq_curr    

        return _max
