'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''



from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndSet = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visited = set('0000')

        while queue:
            curStr, curSteps = queue.popleft()

            if curStr == target:
                return curSteps

            if curStr in deadEndSet:
                continue

            for i in range(4):
                digit = int(curStr[i])
                for dir in [1, -1]:
                    newDigit = (digit + dir) % 10

                    newStr = curStr[:i] + str(newDigit) + curStr[i+1:]

                    if newStr not in visited:
                        visited.add(newStr)
                        queue.append((newStr, curSteps+1))

        return -1
      
-------------------------------------------------------------------------

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(s):
            nei = []
            for i, c in enumerate(s):
                for d in [1, -1]:
                    nei.append(s[:i] + str((int(c)+d) % 10) + s[i+1:])
            return nei    
        deadends = set(deadends)
        if '0000' in deadends: return -1
        if '0000' == target: return 0
        q = deque(['0000'])
        dist = {'0000': 0}
        while q:
            num = q.popleft()
            d = dist[num] + 1
            for nei in neighbors(num):
                if nei not in dist and nei not in deadends:
                    if nei == target:
                        return  d
                    q.append(nei)
                    dist[nei] = d
        return -1
-------------------------------------------------------------------------------      

class Solution:
    def combinations(self, start):
        ans = []
        states = [-1,1]
        
        for i,j in enumerate(start):
            for diff in states:
                val = (int(j) + diff) % 10
                ans.append(start[:i] + str(val) + start[i+1:])
        
        return ans
    
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = '0000'
        q = deque()
        q.append((start, 0))
        vis = set()
        vis.add(start)
        
        while q:
            comb, level = q.popleft()
            
            if comb == target:
                return level
            
            if comb in deadends:
                continue
            
            for newComb in self.combinations(comb):
                if newComb not in vis:
                    vis.add(newComb)
                    q.append((newComb, level+1))
        return -1
--------------------------------------------------------------------------------------------
      
