'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''

class Solution(object):
    def canReach(self, arr, start):
        if(start<0 or start>=len(arr) or arr[start]<0):
            return False
        
        if(arr[start]==0):
            return True
        
        arr[start]=-arr[start]
        ans1 =  self.canReach(arr,start+arr[start])
        ans2 =  self.canReach(arr,start-arr[start])
        
        arr[start] =  -arr[start] # change data back to orginal 
        
        return ans1 or ans2
      
------------------------------------------------------------------------------------
def canReach(self, arr: List[int], start: int) -> bool:
    visited = set()
    def DFS(position):
        if position in visited or position<0 or position>=len(arr):
            return False
        visited.add(position)
        if arr[position] == 0:
            return True
        return DFS(position+arr[position]) or DFS(position-arr[position])

    return DFS(start)
  
---------------------------------------------------------------------------------------------
#bfs

from collections import deque
class Solution:
    def canReach(self, arr, start):
        _len_=len(arr)
        seen=set()
        queue=deque()
        queue.append(start)
        while(queue):
            idx=queue.popleft()
            if arr[idx]==0:
                return True
            seen.add(idx)
            for var in (idx-arr[idx],idx+arr[idx]):
                if (var not in seen) and (-1<var<_len_):
                    queue.append(var)
        return False
      
------------------------------------------------------------------------
from collections import deque
class Solution:
    def dfs(self,arr,idx,seen):
        if idx>=len(arr) or (idx<0) or (idx in seen):
            return False
        if arr[idx]==0:
            return True
        seen.add(idx)
        return self.dfs(arr,idx-arr[idx],seen) or self.dfs(arr,idx+arr[idx],seen)

    def canReach(self, arr, start):
        seen=set()
        return self.dfs(arr,start,seen)
      
---------------------------------------------------------------------------------------------------------   

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = set()
        
        while queue:
            u = queue.pop(0)
            if arr[u] == 0:
                return True
            visited.add(u)
            
            nextjump = u + arr[u]
            if nextjump < len(arr) and nextjump not in visited:
                if arr[nextjump] == 0:
                    return True
                visited.add(nextjump)
                queue.append(nextjump)

            nextjump = u - arr[u]
            if nextjump >= 0 and nextjump not in visited:
                if arr[nextjump] == 0:
                    return True
                visited.add(nextjump)
                queue.append(nextjump)
        return False
