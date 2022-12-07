'''
You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).

Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at least one correct answer.
'''


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ans = []
        for _ in range(n): 
            diff = sums[1] - sums[0]
            ss0, ss1 = [], []
            freq = defaultdict(int)
            on = False 
            for i, x in enumerate(sums): 
                if not freq[x]: 
                    ss0.append(x)
                    freq[x+diff] += 1
                    if x == 0: on = True 
                else: 
                    ss1.append(x)
                    freq[x] -= 1
            if on: 
                ans.append(diff)
                sums = ss0 
            else: 
                ans.append(-diff)
                sums = ss1
        return ans
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        res = []  # Result set
        sums.sort()
        
        while len(sums) > 1:
            num = sums[-1] - sums[-2] # max - secondMax
            countMap = Counter(sums) # Get count of each elements
            excluding = [] # Subset sums that do NOT contain num
            including = [] # Subset sums that contain num
            
            for x in sums:
                if countMap.get(x) > 0:
                    excluding.append(x)
                    including.append(x+num)
                    countMap[x] -= 1
                    countMap[x+num] -= 1
                    
			# Check validity of excluding set	
            if 0 in excluding:
                sums = excluding
                res.append(num)
            else:
                sums = including
                res.append(-1*num)
        
        return res
