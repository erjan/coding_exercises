'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
'''

Then the states and transition function is as below:

First is to calculate a result for all cases:
curr = []  # current sub-list
for m in range(k):  # in total m cases
	curr += dp[i][j-m-1] + max(arr[(j-m):(j+i)]) * (m+1)
dp[i][j-m-1] : is to use the previous dp result for the previous sum
arr[(j-m):(j+i)] : by looking back m+1 numbers to find the max and repeat m+1 times

Then is to choose the max result
dp[i][j] = max(curr)
Since index i in not necessary, we only need j (index of arr), and m (index of k), the script is as below:
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        
        # handle the first k indexes differently
        for j in range(k): dp[j]=max(arr[:j+1])*(j+1)
        
        # we can get rid of index i by running i times
        for j in range(k,n):
            curr = []
            for m in range(k):
                curr.append(dp[j-m-1] + max(arr[(j-m):(j+1)]) * (m+1))
            dp[j] = max(curr)

        return dp[-1]
      
-------------------------------------------------------
This problem is extremely hard to grasp. It's a variation on dynamic programming, but the subproblems are hard to see when you first look at it. I'd say this is a 'Hard' difficulty, not a 'Medium.'

Beginning with the original array [1, 15, 7, 9, 2, 5, 10], the answer to this problem is:
max(1x1 + f([15, 7, 9, 2, 5, 10]), 2x15 + f([7, 9, 2, 5, 10]), + 3x15 + f([9, 2, 5, 10]).
The product at the front is the current 'K' value we are on, multiplied by the maximum value of the first K elements in the array. We have to update the maximum seen so far to multiply it by up to K values of it.

The subproblems themselves just repeat until we reach the empty list, whose answer is 0. After seeing the subproblem, the hard part is getting the indexing correct. Memoization doesn't require this since we can just use a hashtable and store whatever index we are on, but the bottom-up approach does require precise indexing.

We initialize an array of length len(A) + 1. The last element is 0 to represent the base case of the empty list. The element before that is set as A[len(A)-1]. This is because the list with one element's answer is just the one element itself. Each dp[i] represents the answer to the subproblem for the subarray starting at index i. We go in reverse, and using the current max product, we add it to dp[i+k] where k is our offset between 1 and K. We keep taking the max of each iteration.

We check K values per element in our array, so O(NK) runtime. O(N) space.

TOP-DOWN

def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        def recur(arr, start, memo):
            # base case
            if start == len(arr):
                return 0
            
            cur_max = float('-inf')
            res = 0
            
            # we want to loop over k elements, take the maximum and multiply
            # then add it to the corresponding subproblem with the reduced
            # array
            for i in range(K):
                if start+i == len(arr):
                    break
                cur_max = max(cur_max, arr[start+i])
                # take the max of all possibilities
                if start+i+1 in memo:
                    res = max(res, (i+1)*cur_max + memo[start+i+1])
                else:
                    res = max(res, (i+1)*cur_max + recur(arr, start+i+1, memo))
                    
            # return the final result
            memo[start] = res
            return res
        
        memo = {}
        recur(A, 0, memo)
        return memo[0]
BOTTOM-UP

def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [float('-inf') for i in range(len(A)+1)]
        dp[-1] = 0
        dp[-2] = A[-1]
        
        for j in reversed(range(len(A)-1)):
            cur_max = float('-inf')
            for k in range(K):
                if j+k == len(A):
                    break
                cur_max = max(cur_max, A[j+k])
                dp[j] = max(dp[j], (k+1)*cur_max + dp[j+k+1])
        
        return dp[0]
