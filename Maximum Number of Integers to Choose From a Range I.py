You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.
  -----------------------------------------------------------------------------------------------------------

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        arr = [i for i in range(1, n+1)]

        banned = set(banned)
        cursum = 0
        cnt = 0
        for el in arr:
            if el not in banned and cursum+el<=maxSum:
                banned.add(el)
                cursum+=el
                cnt+=1


        return cnt


