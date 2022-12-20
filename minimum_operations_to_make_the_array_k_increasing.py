'''
You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.

The array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.

For example, arr = [4, 1, 5, 2, 6, 2] is K-increasing for k = 2 because:
arr[0] <= arr[2] (4 <= 5)
arr[1] <= arr[3] (1 <= 2)
arr[2] <= arr[4] (5 <= 6)
arr[3] <= arr[5] (2 <= 2)
However, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).
In one operation, you can choose an index i and change arr[i] into any positive integer.

Return the minimum number of operations required to make the array K-increasing for the given k.
'''

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        def lis(nums):
            '''
            Patience sort
            Time: O(NlogN)
            Space: O(N)
            '''
            n = len(nums)
            if n <= 1:
                return n
            # num, pointer
            c = []
            size = 0

            for x in nums:
			    # bisect as it is non-decreasing
                l = bisect.bisect_right(c, x)
                if l < size:
                    c[l] = x
                else:
                    c.append(x)
                    size = max(size, l+1)

            return size
        
        ans = 0
        for i in range(k):
            sub = []
            for j in range(i, n, k):
                sub.append(arr[j])
            ans += len(sub) - lis(sub)
        
        return ans
      
---------------------------------------------------------------------------------------------------------------------
class Solution:
    
    def LIS(self, arr):
        n = len(arr)
        dp = ['None']*n
        dp[0] = arr[0]
        j= 0 
        for i in range(1,n):
            if arr[i]>=dp[j]:
                dp[j+1] = arr[i]
                j+=1
            else:
                idx = bisect.bisect(dp,arr[i],0,j) # log(n)
                dp[idx] = arr[i]
        count = 0
        for i in dp:
            if i=='None':
                break
            count+=1
        return count

        
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        n  = len(arr)
        for i in range(k):
            nums = []
            for j in range(i,n,k):
                nums.append(arr[j])
            ans+=(len(nums)-self.LIS(nums))
            
        return ans
        
        
        
