'''
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

'''
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left = [0]*len(capacity)
        for i in range(len(capacity)):
            left[i] = capacity[i]-rocks[i]
        left.sort()
        ans = 0 
        while ans < len(left) and additionalRocks > 0:
            if additionalRocks >= left[ans]:
                additionalRocks -= left[ans]
                ans += 1
            else:
                break
        return ans
      
-------------------------------------------------------------------------------------------
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        res = []
        for i in range(len(capacity)):
            res.append(capacity[i] - rocks[i])
            
        res.sort()
        count = 0
        
        for i in range(len(res)):
            if res[i] == 0:
                count += 1
            elif additionalRocks >= res[i]:
                additionalRocks -= res[i]
                count += 1
        
        return count
