'''
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.
'''


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @cache
        def dp(l, r, count = 0):
            if l > r: return 0
            // Initial count for the letter at boxes[l]
            count += 1
            ptr = l + 1
            while ptr <= r and boxes[l] == boxes[ptr]:
                ptr += 1
                count += 1
            points = (count ** 2) + dp(ptr, r)
            for i in range(ptr + 1, r + 1):
                if boxes[l] == boxes[i]:
                    points = max(points, dp(i, r, count) + dp(ptr, i - 1))
            return points

        return dp(0, len(boxes) - 1)
      
----------------------------------------------------------------------------------------------
from collections import defaultdict
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        ind_dict = defaultdict(list)
        
        for i in reversed(range(len(boxes))):
            ind_dict[boxes[i]].append(i)
        
        @lru_cache(maxsize = None)
        def dfs(i, j, count):
            
            if j-i<1:
                return 0
            
            forward_val = (count+1)**2 + dfs(i+1, j, 0)
            jump_val = 0
            for ind in ind_dict[boxes[i]]:
                if ind>i and ind<j:
                    temp =dfs(ind, j, count +1)+dfs(i+1, ind, 0)
                    jump_val = max(jump_val, temp)
            return max(jump_val, forward_val)
            
        res = dfs(0, len(boxes), 0)
        
        return res
      
