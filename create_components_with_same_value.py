'''
There is an undirected tree with n nodes labeled from 0 to n - 1.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.

Return the maximum number of edges you can delete, such that every connected component in the tree has the same value.
'''

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        tree = [[] for _ in nums]
        for u, v in edges: 
            tree[u].append(v)
            tree[v].append(u)
        
        def fn(u, p):
            """Post-order dfs."""
            ans = nums[u]
            for v in tree[u]: 
                if v != p: ans += fn(v, u)
            return 0 if ans == cand else ans
        
        total = sum(nums)
        for cand in range(1, total//2+1): 
            if total % cand == 0 and fn(0, -1) == 0: return total//cand-1
        return 0 
      
------------------------------------------------------------------------------------------

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        
        def dfs(u: int) -> int:
     

            self.visit[u] = True
            currComponentNode = 0

            for i in range(len(self.g[u])):
                v = self.g[u][i]

                if (not self.visit[v]):

                    subtreeNodeCount = dfs(v)
                    
                    if subtreeNodeCount == -1:
                        return -1

                    if (subtreeNodeCount == self.count):
                        self.res += 1

                    else:
                        currComponentNode += subtreeNodeCount
                        
                        if currComponentNode > self.count:
                            return -1

            return currComponentNode + nums[u]


        def maxEdgeRemovalToMakeForest(N: int) -> int:


            self.visit = [False for _ in range(N + 1)]
            
            self.res = 0
            
            d = dfs(0)
            
            if d == -1:
                return 0
                #return self.res
            
            if d == self.count:
                return self.res
            
            if d != self.count :
                return 0

            return self.res

        def addEdge(u: int, v: int) -> None:


            self.g[u].append(v)
            self.g[v].append(u)
 
        res = 0

        N = len(nums)
        E = len(edges)
        

        r = 0
        for i in range(1, max(51, N )):
            
            
            self.count = i
            self.g = [[] for _ in range(N)]
            
            for j in range(E):
                
                addEdge(edges[j][0], edges[j][1])
            
            c = maxEdgeRemovalToMakeForest(N)
            r = max( r,  c )
            

        return r
		
----------------------------------------------------------------------------------------------------------------
class Solution:
    def getFactors(self, x):
        factors = []
        for i in range(1, int(sqrt(x)) + 1):
            if x % i != 0: continue
            factors.append(i)
            if x // i != i: factors.append(x // i)
        return factors

    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.cntRemainZero = 0
        def dfs(u, p, sumPerComponent): # return remain of the subtree with root `u`
            remain = nums[u]
            for v in graph[u]:
                if v == p: continue
                remain += dfs(v, u, sumPerComponent)
                
            remain %= sumPerComponent
            if remain == 0:
                self.cntRemainZero += 1
                
            return remain
        
        def isGood(sumPerComponent, expectedNumOfComponents):
            self.cntRemainZero = 0
            dfs(0, -1, sumPerComponent)
            return self.cntRemainZero == expectedNumOfComponents
        
        sumAllNodes, maxNum = sum(nums), max(nums)
        for sumPerComponent in sorted(self.getFactors(sumAllNodes)):
            if sumPerComponent < maxNum: continue  # at least maxNum
            expectedNumOfComponents = sumAllNodes // sumPerComponent
            if isGood(sumPerComponent, expectedNumOfComponents):
                return expectedNumOfComponents - 1 # Need to cut `numOfComponent - 1` edges to make `numOfComponent` connected component
            
        return 0
