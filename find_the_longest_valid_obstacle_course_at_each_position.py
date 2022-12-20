'''
You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

You choose any number of obstacles between 0 and i inclusive.
You must include the ith obstacle in the course.
You must put the chosen obstacles in the same order as they appear in obstacles.
Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.
'''

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans, vals = [], []
        for i, x in enumerate(obstacles): 
            k = bisect_right(vals, x)
            ans.append(k+1)
            if k == len(vals): vals.append(x)
            else: vals[k] = x
        return ans 
      
-----------------------------------------------------------------------------------------------
class Fenwick: 
    def __init__(self, n): 
        self.data = [0]*(n+1)

    def query(self, k): 
        k += 1
        ans = 0 
        while k:
            ans = max(ans, self.data[k])
            k -= k & (-k)
        return ans 
            
    def update(self, k, x): 
        k += 1
        while k < len(self.data): 
            self.data[k] = max(self.data[k], x)
            k += k & (-k)

            
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # compress numbers into smaller range
        ss = sorted(set(obstacles))
        mp = dict(zip(ss, range(len(ss))))
        
        ans = []
        fen = Fenwick(len(ss))
        for x in obstacles: 
            val = fen.query(mp[x])+1
            ans.append(val)
            fen.update(mp[x], val)
        return ans 
      
-------------------------------------------------------------------------------------------------
class Solution:
def longestObstacleCourseAtEachPosition(self, obs: List[int]) -> List[int]:
    local = []
    res=[0 for _ in range(len(obs))]
    for i in range(len(obs)):
        n=obs[i]
        if len(local)==0 or local[-1]<=n:
            local.append(n)
            res[i]=len(local)
        else:
            ind = bisect.bisect_right(local,n)
            local[ind]=n
            res[i]=ind+1
    
    return res
