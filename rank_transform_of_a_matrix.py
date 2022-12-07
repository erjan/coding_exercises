'''
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

The rank is an integer starting from 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
The test cases are generated so that answer is unique under the given rules.
'''

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) # dimension 
        # mapping from value to index 
        mp = {} 
        for i in range(m):
            for j in range(n): 
                mp.setdefault(matrix[i][j], []).append((i, j))
        
        def find(p):
            """Find root of p."""
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]
        
        rank = [0]*(m+n)
        ans = [[0]*n for _ in range(m)]
        
        for k in sorted(mp): # from minimum to maximum 
            parent = list(range(m+n))
            for i, j in mp[k]: 
                ii, jj = find(i), find(m+j) # find 
                parent[ii] = jj # union 
                rank[jj] = max(rank[ii], rank[jj]) # max rank 
            
            seen = set()
            for i, j in mp[k]:
                ii = find(i)
                if ii not in seen: rank[ii] += 1
                seen.add(ii)
                rank[i] = rank[m+j] = ans[i][j] = rank[ii]
        return ans 
      
---------------------------------------------------------------------------------
Use Union Find to union points with same value in the same row/column, make one point to be the the other's parent
Ex. A = 10, B = 10, and they are in the same row/column, then parent[A] = [A], parent[B] = A
Use Graph & Topological Sort to connect unique "root" points that parent[point] = point itself by points' values
Ex. -21 -> 14 -> 20
Use BFS Queue to rank those "root" points, then we got some of the ranks
Add back points that parent[point] != point itself, then we got all the ranks
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        def find_root(x: int, y: int):
            if parent[x][y] == (x, y):
                return (x, y)
            else:
                r = find_root(parent[x][y][0], parent[x][y][1])
                parent[x][y] = r
                return r
        
        def union(x1, y1, x2, y2):
            root_a = find_root(x1, y1)
            root_b = find_root(x2, y2)
            parent[root_b[0]][root_b[1]] = root_a
            
        ########################################################
        
		# *parent* records the parent of each point in matrix form
		# points with same value in the same row/column should have the same parent
        parent = [[(j, i) for i in range(n)] for j in range(m)]
        
		# sort each row, if there are points with same value, union them
        for i in range(m):
            value = []
            for j in range(n):
                v = tuple([matrix[i][j], i, j])
                value.append(v)
            value.sort()
            for k in range(n - 1):
                if value[k][0] == value[k + 1][0]:
                    union(value[k][1], value[k][2], value[k + 1][1], value[k + 1][2])
					
        # sort each column, if there are points with same value, union them            
        for i in range(n):
            value = []
            for j in range(m):
                v = tuple([matrix[j][i], j, i])
                value.append(v)
            value.sort()
            for k in range(m - 1):
                if value[k][0] == value[k + 1][0]:
                    union(value[k][1], value[k][2], value[k + 1][1], value[k + 1][2])
        
        ########################################################
        
        dic = {} # point index : point that it directs ->
        in_degree = {} # point index : number of incoming arrows <-
		
		# Ex. [20, -21, 14]
		# sort: -21 (0, 1) -> 14 (0, 2) -> 20 (0, 0)
		# dic = { (0, 0) : [], (0, 1) : [(0, 2)], (0, 2) : [(0, 0)] }
		# in_degree = { (0, 0) : 1, (0, 1) : 0, (0, 2) : 1 }
		
		# only select "root" points that parent[point] = point itself
        for i in range(m):
            for j in range(n):
                if parent[i][j] == (i, j):
                    dic[(i, j)] = []
                    in_degree[(i, j)] = 0
                    
		# if there are points that parent[point] = its parent but not the "root" ancestor
		# make parent[point] = the "root" ancestor
		
		# Ex. before: parent[4][4] = (4, 4), parent[8][0] = (4, 4), parent[8][4] = (8, 0)
		# after: parent[4][4] = (4, 4), parent[8][0] = (4, 4), parent[8][4] = (4, 4)
		
        for i in range(m):
            for j in range(n):
                while parent[i][j] not in dic:
                    parent[i][j] = parent[parent[i][j][0]][parent[i][j][1]]
        
		# continue to construct *dic* and *in_degree*
		# make connections in each row
        for i in range(m):
            row = []
            for j in range(n):
                r = tuple([matrix[i][j], parent[i][j][0], parent[i][j][1]])
                row.append(r)
            row.sort()
            for k in range(n - 1):
                if row[k][0] < row[k + 1][0]:
                    if (row[k][1], row[k][2]) in dic and (row[k + 1][1], row[k + 1][2]) in dic:
                        if (row[k + 1][1], row[k + 1][2]) not in dic[(row[k][1], row[k][2])]:
                            dic[(row[k][1], row[k][2])].append((row[k + 1][1], row[k + 1][2]))
                            in_degree[(row[k + 1][1], row[k + 1][2])] += 1
        
		# and make connections in each column
        for i in range(n):
            col = []
            for j in range(m):
                c = tuple([matrix[j][i], parent[j][i][0], parent[j][i][1]])
                col.append(c)
            col.sort()
            for k in range(m - 1):
                if col[k][0] < col[k + 1][0]:
                    if (col[k][1], col[k][2]) in dic and (col[k + 1][1], col[k + 1][2]) in dic:
                        if (col[k + 1][1], col[k + 1][2]) not in dic[(col[k][1], col[k][2])]:
                            dic[(col[k][1], col[k][2])].append((col[k + 1][1], col[k + 1][2]))
                            in_degree[(col[k + 1][1], col[k + 1][2])] += 1
        
        #######################################################################
        
		# *distance* records the rank of the "root" points (just my naming habit)
        distance = {} # point index : rank
        for i in range(m):
            for j in range(n):
                if parent[i][j] == (i, j):
                    distance[(i, j)] = 0
        
		# first put "root" points that have 0 in_degree (meaning they are the smallest) in queue
        queue = []
        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)
                distance[i] = 1
        
        head = 0
        tail = len(queue) - 1
        while head <= tail:
            h = queue[head]

            for p in dic[h]:
                in_degree[p] -= 1
                if in_degree[p] == 0:
                    queue.append(p)
                    distance[p] = distance[h] + 1

            head += 1
            tail = len(queue) - 1
        
        #######################################################################
        
		# *rank* records the final result in matrix form
        rank = [[0 for i in range(n)] for j in range(m)]
        
		# now we already got the rank of those "root" points recorded in *distance*
		# let's put them in *rank*, also their descendants'
        for i in range(m):
            for j in range(n):
                rank[i][j] = distance[parent[i][j]]
        
        return rank
