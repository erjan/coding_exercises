'''
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 
 '''

class Solution:
    def shortestDistanceColor(self, c: List[int], q: List[List[int]]) -> List[int]:
    	C, A = {}, []
    	for i,j in enumerate(c):
    		if j in C: C[j].append(i)
    		else: C[j] = [i]
    	for [i,d] in q:
    		if d not in C:
    			A.append(-1)
    			continue
    		I = bisect.bisect(C[d],i)
    		A.append(min(abs(i-C[d][I-1]),abs(i-C[d][min(I,len(C[d])-1)])))
    	return(A)
    
----------------------------------

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, v in enumerate(colors): d[v].append(i)
        
        def search(i,c):
            if c not in d: return -1
            j = bisect.bisect(d[c], i)
            if j==len(d[c]): return i - d[c][-1]
            if j==0: return d[c][0] - i
            return min(d[c][j] - i, i - d[c][j-1])
        return [search(i, c) for i, c in queries]
------------------------------------------------------------

Explanation
Store all indices of each color in a list dictionary[color] = [idx1, idx2 ....]
Use binary search to help query
Handle the edge cases (index out of bound etc.)
Return -1 if there is not index have a color
Implementation
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for i, color in enumerate(colors): d[color].append(i)
        ans, ld = [], {i: len(d[i]) for i in range(1, 4)}    
        for (start, color) in queries:
            if not d[color]: ans.append(-1)
            else:    
                idx = bisect.bisect_left(d[color], start)
                left, right = sys.maxsize, sys.maxsize
                if idx > 0: left = start-d[color][idx-1] 
                if idx < ld[color]: right = d[color][idx]-start
                ans.append(min(left, right))
        return ans  
---------------------------------------------------------------

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        indices = [[] for _ in range(3)]
        for i, c in enumerate(colors):
            indices[c-1].append(i)
        ans = []    
        for i, c in queries:
            if colors[i] == c:
                ans.append(0)
            elif not indices[c-1]:
                ans.append(-1)
            else:    
                j = bisect.bisect(indices[c-1], i)
                dist = len(colors)
                if j > 0:
                    dist = min(dist, i - indices[c-1][j-1])
                if j < len(indices[c-1]):
                    dist = min(dist, indices[c-1][j] - i)
                ans.append(dist)    
        return ans 
------------------------------------------------------------------------------

Declared 3 list to store nearest steps for 3 colors.
Two scan (from left +from right) done to store the minimum value from both sides in the array.
def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ones,twos,threes = [0]*len(colors), [0]*len(colors), [0]*len(colors)
        a,b,c = 9999999,9999999,9999999
        for i in range(len(colors)):
            if colors[i] == 1:
                a = 0
            elif colors[i] == 2:
                b = 0
            elif colors[i] == 3:
                c = 0
            ones[i], twos[i],threes[i] = a,b,c
            a+=1
            b+=1
            c+=1
        for i in range(len(colors)-1,-1,-1):
            if colors[i] == 1:
                a = 0
            elif colors[i] == 2:
                b = 0
            elif colors[i] == 3:
                c = 0
            ones[i], twos[i],threes[i] = min(ones[i],a),min(twos[i],b),min(threes[i],c)
            a+=1
            b+=1
            c+=1
        for i in range(len(colors)):
            if ones[i] >= 9999999: ones[i] = -1
            if twos[i] >= 9999999: twos[i] = -1
            if threes[i] >= 9999999: threes[i] = -1
        res = []
        for i in range(len(queries)):
            if queries[i][1] == 1: res.append(ones[queries[i][0]])
            elif queries[i][1] == 2: res.append(twos[queries[i][0]])
            elif queries[i][1] == 3: res.append(threes[queries[i][0]])
        return res
-----------------------------------------------------------------------------

class Solution:
	def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
		self.dic=set(colors)
		self.memo={}
		res=[self.helper(colors,a,b) for a,b in queries]
		return res

	def helper(self,colors,a,b):
		if (a,b) in self.memo:
			return self.memo[(a,b)]
		if b not in self.dic:
			return -1
		right=float('inf')
		left=float('inf')
		for i in range(a,len(colors)):
			if colors[i]==b:
				right=i-a
				break
		for i in range(a,-1,-1):
			if colors[i]==b:
				left=a-i
				break
		ans=min(left,right)
		self.memo[(a,b)]=ans
		return min(left,right)
      
      
      
      
    
