'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ans = ii = total = 0 
        for x in nums: 
            total += freq[x]
            freq[x] += 1
            while total >= k: 
                freq[nums[ii]] -= 1
                total -= freq[nums[ii]]
                ii += 1
            ans += ii 
        return ans 
      
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        D = defaultdict(int)
        ans = cnt = l = 0
        for i in A:
            cnt += D[i]
            D[i] += 1
            while cnt >= k:
                D[A[l]] -= 1
                cnt -= D[A[l]]
                l += 1
            ans += l
        return ans
      
----------------------------------------------------------------------------------------------------
'''
Here's the plan:

We incrementright and use a dict d to keep track of the count of each integer in nums[:right+1].
Once the number of pairs reachesk, we add the count of subarrays with subarray [right+1]toans].
We incrementleftand adjustd. If we still havekpairs, we add a similar count to ansand increment leftagain. If not, we iteraterightand start again.
Oncerightiteratesnumscompletely andleftincrements so that pairs are less thank, we return ans.
'''

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        left = ans = tally = 0
        n, d = len(nums), defaultdict(int)

        for right,num in enumerate(nums):    # <-- 1
            tally += d[num]
            d[num] += 1
            
            while tally >= k:                # <-- 2     
                ans+= n - right
                d[nums[left]] -= 1           # <-- 3
                tally -= d[nums[left]]
                left += 1
            
        return ans                           # <-- 4
