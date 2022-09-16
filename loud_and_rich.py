'''
There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different level of quietness.

You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x.

 
 '''

def loudAndRich(richer, quiet):
	g, loud = collections.defaultdict(set), [-1]*len(quiet)
	for u, v in richer: g[v].add(u)
	def dfs(node):
		if loud[node] < 0: loud[node] = min([dfs(nei) for nei in g[node]]+[node], key=lambda x:quiet[x])
		return loud[node]
	return list(map(dfs, range(len(quiet))))

-----------------------------------------
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        length = len(quiet)
        arr = [i for i in range(length)]
        indegree = [0 for _ in range(length)]
        graph = collections.defaultdict(list)
        dq = collections.deque([])
        
        for a, b in richer:
            # Note that the graph is uni-directional
            graph[a].append(b)
            indegree[b] += 1

        for i in range(length):
            if not indegree[i]: 
                dq.append(i)
    
        while dq:
            node = dq.popleft()
            
            for vertex in graph[node]:
                indegree[vertex] -= 1
                if quiet[arr[node]] < quiet[arr[vertex]]:
                    arr[vertex] = arr[node]
                if not indegree[vertex]:
                    dq.append(vertex)
        return arr
      
-----------------------------------------------------------

class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        
        def find_quietest(i):
            
            #recursively visit all the neighbors of i and calculate least noisy
            #sinc we have to apply min ops on the quiet[node_number]; we are storing both node_num and val of quiet[node_number]
            #for instance dict1 = {0: [1], 1: [2, 3], 3: [4, 5, 6], 7: [3]}
            #queit = [3,2,5,4,6,1,7,0]
            '''
            for node 0: we take min((0, 3), find_quietest(1)) --> min((0, 3), (5, 1)) --> (5,1)
            find_quietest(1) = min((1, 2), find_quietest(2), find_quietest(3))
                             = min((1, 2), (2, 5), (5, 1))
                             = (5, 1)
            find_quietest(2) = (2, 5)
            find_quietest(3) = min((3, 4), find_quietest(4), find_quietest(5), find_quietest(6)) 
                             = min((3,4), (4,6), (5,1), (6,7))
                             = (5,1)
            find_quietest(4) = (4, 6)
            find_quietest(5) = (5, 1)
            find_quietest(6) = (6, 7)
            
            '''
            
            if i in memo:
                return memo[i]
            
            #as no information has been given about i
            if i not in dict1:
                return (i, quiet[i])
            
            quietest = (i, quiet[i])
            
            for richer in dict1[i]:
                quietest = min(quietest, find_quietest(richer), key= lambda x: x[1])
            
            return quietest
        
        #base 
        if len(quiet) == 1:
            return quiet
        
        dict1 = {}
        memo = {}
        
        
        #Convert richer into a directed graph
        #For example: [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
        #dict[0] = [1] which indicates 1 has more money than 0
        #so value at key x is all people richer than x
        for val in richer:
            if val[1] in dict1:
                dict1[val[1]].append(val[0])
            else:
                dict1[val[1]] = [val[0]]
        
        
        #create a copy of quiet as every person will be either itself or least quiet between itself and all its richer neighbors  
        result = list(quiet)
        
        for i in range(len(quiet)):
            #navigate all the neighbors richer than the node
            output = find_quietest(i)
            result[i] = output[0]
            #used for memoization
            memo[i] = output
        
        return result
