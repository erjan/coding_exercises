'''
You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.
'''


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: defaultdict(int))
        for i, x in enumerate(nums): freq[i%k][x] += 1 # freq by row
        
        n = 1 << 10
        dp = [0] + [-inf]*(n-1)
        for i in range(k): 
            mx = max(dp)
            tmp = [0]*n
            for x, c in enumerate(dp): 
                for xx, cc in freq[i].items(): 
                    tmp[x^xx] = max(tmp[x^xx], c + cc, mx)
            dp = tmp 
        return len(nums) - dp[0]
      
--------------------------------------------------------------------------------------

def minChanges(self, nums: List[int], k: int) -> int:

    LIMIT = 2**10
    mrr = [[0 for _ in range(LIMIT)] 
           for _ in range(k)]
    for i,x in enumerate(nums):
        mrr[i%k][x] += 1

    dp = [-2000 for _ in range(LIMIT)]
    dp[0] = 0
    for row in mrr:
        maxprev = max(dp)
        new_dp = [maxprev for _ in range(LIMIT)]
        for i,cnt in enumerate(row):
            if cnt > 0:
                for j,prev in enumerate(dp):
                    new_dp[i^j] = max(new_dp[i^j], prev+cnt)
        dp = new_dp

    return len(nums) - new_dp[0]
