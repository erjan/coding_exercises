'''
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
'''

class Solution:
    def buildMatrix(self, k: int, rc: List[List[int]], cc: List[List[int]]) -> List[List[int]]:
        def toposortBFS(cond):
            adj=[[] for i in range(k+1)]
            for u,v in cond:
                adj[u].append(v)
            inDegree=[0 for i in range(k+1)]
            topoArray=[]
            q=[]
            for i in range(1,k+1):
                for j in adj[i]:
                    inDegree[j]+=1
            for i in range(1,k+1):
                if inDegree[i]==0:
                    q.append(i)
            while q:
                ele=q.pop(0)
                topoArray.append(ele)
                for it in adj[ele]:
                    inDegree[it]-=1
                    if inDegree[it]==0:
                        q.append(it)
            return topoArray
        t1=toposortBFS(rc)
        t2=toposortBFS(cc)
        if len(t1)<k or len(t2)<k:
            return []
        ans=[[0 for i in range(k)] for i in range(k)]
        hmap=defaultdict(list)
        for ind,x in enumerate(t1):
            hmap[x].append(ind)
        for ind,x in enumerate(t2):
            hmap[x].append(ind)
        for key in hmap.keys():
            x,y=hmap[key]
            ans[x][y]=key
        return ans
            
------------------------------------------------------------------------------------------------------------------
class Solution:
    def buildMatrix(self, n: int, rowC: List[List[int]], colC: List[List[int]]) -> List[List[int]]:
		# create two graphs, one for row and one for columns
        row_adj = {i: [] for i in range(1, n + 1)}
        col_adj = {i: [] for i in range(1, n + 1)}
        for u, v in rowC:
            row_adj[u].append(v)
        for u, v in colC:
            col_adj[u].append(v)
            
        # inorder to do topological sort, we need to maintain two visit lists: one marks which node 
        # we have already processed (because not all nodes are connected to each other and we do not 
        # want to end up in a infinite loop), the other one marks nodes we are currently visiting(or in 
        # our recursion stack). If we visit a node that we are currently visiting, that means there is 
        # a loop, so we return False; if it is not in our current visit but has already been visited, we 
        # can safely travel to the next node and return True. 

        row_stack = []
        row_visit = set()
        row_visiting = set()
        col_stack = []
        col_visit = set()
        col_visiting = set()
        
        def dfs(node, stack, visit, visiting, adj):
            if node in visiting:
                return False
            if node in visit:
                return True
            visit.add(node)
            visiting.add(node)
            for child in adj[node]:
                if not dfs(child, stack, visit, visiting, adj):
                    return False
            visiting.remove(node)
            stack.append(node)
            return True
        
        # do dfs on each row/col graph
        for i in range(1, n + 1):
            if i not in row_visit:
                if not dfs(i, row_stack, row_visit, row_visiting, row_adj):
                    return []
            if i not in col_visit:
                if not dfs(i, col_stack, col_visit, col_visiting, col_adj):
                    return []

		    

        # After the dfs, we also need a stack to store which node has been entirely explored. That's why we 
        # append the current node to our stack after exploring all its neighbors. Remember we have to reverse 
        # the stack after all DFS's, because the first-explored node gets appended first. 
        row_stack, col_stack = row_stack[::-1], col_stack[::-1]
        
        
        # mark position for each element
        row_memo, col_memo = {}, {}
        for idx, num in enumerate(row_stack):
            row_memo[num] = idx
        for idx, num in enumerate(col_stack):
            col_memo[num] = idx
            
        # create an empty matrix as our ans
        ans = [[0]*n for _ in range(n)]
        
        # plug in values from what we have discovered
        for i in range(1, n + 1):
            ans[row_memo[i]][col_memo[i]] = i
        return ans
      
------------------------------------------------------------------------------------------------------------------------

        
        
