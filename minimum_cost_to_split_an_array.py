'''
You are given an integer array nums and an integer k.

Split the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray in the split.

Let trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.

For example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].
The importance value of a subarray is k + trimmed(subarray).length.

For example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray will be k + 5.
Return the minimum possible cost of a split of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
'''



class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        dp=[0]
        nums=[-1]+nums
        def main(i):
            mp=defaultdict(int)
            s=0
            ans=10000000000000
            while i>0:
                if mp[nums[i]]>0:
                    s+=1
                    if mp[nums[i]]==1:
                        s+=1
                mp[nums[i]]+=1
                ans=min(dp[i-1]+s,ans)
                i-=1
            return ans+k
                
            
        for i in range(1,len(nums)):
            dp.append(main(i))
        return dp[-1]
      
------------------------------------------------------------------------------------------------
class Solution:                                         #   Example: nums = [1, 2, 1, 2] 5
    def minCost(self, nums: List[int], k: int) -> int:  #
                                                        #   left   right   tmp   ans     nums[left,right+1]
        @lru_cache(None)                                #   ––––   ––––   ––––   ––––    ––––––––––––––––––  
        def dp(left, n = len(nums)):                    #     0      3      9      9 <-- [1, 2, 1, 2]
                                                        #     0      2      7     10     [1, 2, 1]
            if left == n: return 0                      #     0      1      5     10     [1, 2]
                                                        #     0      0      5     12     [1]
            tmp, ans,d = k, inf, defaultdict(int)       #     1      3      7      7     [2, 1, 2]
                                                        #     1      2      5     10     [2, 1]
            for right, num in enumerate(                #     1      1      5     10     [2]
                       nums[left:], start = left):      #     2      3      5      5     [1, 2]
                                                        #     2      2      5     10     [1]
                d[num]+= 1                              #     3      3      5      5     [2]
                tmp+= (d[num] > 1) + (d[num] == 2)
                ans = min(ans, tmp + dp(right+1))
                
            return ans

        return dp(0)  
