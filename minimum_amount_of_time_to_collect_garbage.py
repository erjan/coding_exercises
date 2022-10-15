'''
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
'''


    def garbageCollection(self, A: List[str], travel: List[int]) -> int:
        last = {c: i for i,pgm in enumerate(A) for c in pgm}
        dis = list(accumulate(travel, initial = 0))
        return sum(map(len, A)) + sum(dis[last.get(c, 0)] for c in 'PGM')
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        from collections import defaultdict

        ans = 0
        lastH = {}
        num = defaultdict(int)

        for i in range(len(garbage)):
            for char in garbage[i]:
                num[char] += 1
                lastH[char] = i
                
        pref = []
        res = 0
        for x in travel:
            res += x
            pref.append(res)

        ans = sum(num.values())
        for k, v in lastH.items():
            if lastH[k] != 0:
                ans += pref[lastH[k] - 1]
            
        return ans
      
