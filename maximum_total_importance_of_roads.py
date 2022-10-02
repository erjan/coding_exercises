'''
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.
'''


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        '''The main idea is to count the frequency of the cities connected to roads and then 
           keep on assigning the integer value from one to n to each cities after sorting it. '''
        
        f = [0 for _ in range(n)]   # for storing the frequency of each city connected to pathways
        
        for x, y in roads:
            f[x] += 1
            f[y] += 1
        
        f.sort()
        s = 0
        for i in range(len(f)):
            s += f[i] * (i+1)  # assigning and storing the integer value to each cities frequency in ascending order
        return s
        
----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        Arr = [0] * n  # i-th city has Arr[i] roads
        for A,B in roads:
            Arr[A] += 1 # Each road increase the road count
            Arr[B] += 1
        Arr.sort()  # Cities with most road should receive the most score
        summ = 0
        for i in range(len(Arr)):
            summ += Arr[i] * (i+1)  # Multiply city roads with corresponding score
        
        return summ
