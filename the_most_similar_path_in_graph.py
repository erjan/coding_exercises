'''
We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai with city bi. Each city has a name consisting of exactly three upper-case English letters given in the string array names. Starting at any city x, you can reach any city y where y != x (i.e., the cities and the roads are forming an undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph of the same length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance. The path should be of the same length of targetPath and should be valid (i.e., there should be a direct road between ans[i] and ans[i + 1]). If there are multiple answers return any one of them.

'''

from collections import defaultdict
from functools import cache

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        name_to_idx = defaultdict(set)
        for i, name in enumerate(names):
            name_to_idx[name].add(i)
        conn = defaultdict(list)
        for a, b in roads:
            conn[a].append(b)
            conn[b].append(a)
        
        @cache
        def dp(i, length):
            edit = 0 if i in name_to_idx.get(targetPath[-length], [-1]) else 1
            if length == 1:
                return (edit, [i])
            cost, path = min([dp(j, length-1) for j in conn[i]], key=lambda x:x[0])
            return (edit + cost, [i] + path)
        
        
        cost, path = min([dp(i, len(targetPath)) for i in range(n)], key=lambda x:x[0])
        return path
      
      
---------------------
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # algorithm: dynamic programming
        # step1: build graph through adjacent matrix
        # step2: run dp to get the minimum cost
        # step3: rebuild graph
        # if we would like to know the min cost for city v at targetPath i
        # we need to know the min cost for cities u connecting to city v at targetPath i-1
        # cost(v, targetPath i) = min(cost(cities_connect_u, targetPath i-1))+possible_edit_cost(v) 
        # time complexity:  O(m*n^2) 
        # space complexity: O(n(n+m))
        
        m = len(targetPath)
        
        # build graph
        graph = [[] for i in range(n)]
        for r in roads:
            graph[r[0]].append(r[1])
            graph[r[1]].append(r[0])
        # idx negative one for dummy
        graph.append([i for i in range(n)])
        
        # idx zero for dummy
        dp = [[10**9]*n for i in range(m+1)]
        dp[0] = [0]*n
        paths = [[-1]*n for i in range(m)]
        
        # each target i in the target path
        for i in range(1, m+1):
            # each city
            # calculate the cost for each at target i
            for v in graph[-1]:
                # use dp to calculate it
                for u in graph[v]:
                    if dp[i][v]>dp[i-1][u]:
                        dp[i][v] = dp[i-1][u]
                        paths[i-1][v] = u
                dp[i][v] += names[v]!=targetPath[i-1]
        
        # get the final city from dp table
        res = [-1]
        endCost = 10**9
        for i in range(n):
            if endCost>dp[m][i]:
                endCost = dp[m][i]
                res[0] = i
         
        # rebuild the path from final city to first city
        for i in range(m-1, 0, -1):
            res.append(paths[i][res[-1]])
        
        return res[::-1]
      
      
-----------------------------------------------------------------

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        path_length = len(targetPath)
        ajl = collections.defaultdict(set)
        for src, dest in roads:
            ajl[src].add(dest)
            ajl[dest].add(src)
        
        @functools.lru_cache(None)
        def min_distance_with_given_end_city(target_idx, end_city_idx):
            '''returns the min distance and the id of the source city for the path ending in end_city_idx'''
            city_cost = 1 - (targetPath[target_idx] == names[end_city_idx])
            if target_idx == 0: return city_cost, None  # there is no source city for the first city in the path
            
            mindist = path_length
            srccity = None
            for source_city_idx in ajl[end_city_idx]:
                distfrom, fromcity = min_distance_with_given_end_city(target_idx - 1, source_city_idx)
                if distfrom < mindist:
                    mindist = distfrom
                    srccity = source_city_idx
                    
            return mindist + city_cost, srccity
        
        # now let's start from the last city in the path and find the route back which has minimum cost
        target_position = path_length - 1
        last_city_choices = [(min_distance_with_given_end_city(target_position, end_city_idx), end_city_idx) \
                             for end_city_idx in range(n)]
        (mindist, src_city_idx), end_city_idx = min(last_city_choices)
        
        route = collections.deque([end_city_idx])
        while src_city_idx is not None:
            route.appendleft(src_city_idx)
            target_position -= 1
            mindist, src_city_idx = min_distance_with_given_end_city(target_position, src_city_idx)
        
        return route
