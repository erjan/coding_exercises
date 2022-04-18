'''
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.
'''


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
	"""
        ## APPROACH : DP ##
        ## INTUITION : started with dp matrix, if chars match, take dp[i-1][j-1] if they dont take 1 + max(dp[i][j-1], dp[i-1][j])
        ## This didnot work for my manual test case: 224524, where best case is 5, 424, 22
        ## But if we do only checks for i-1 and j-1 it is not enough as we are only checking sub problems (2, 24524) and (22452, 4). Here the best case comes for sub problems 22, 4524 ==> 1 + 2 = 3. ( This is when I relealized that not only dp[i-1], dp[j-1] we have to check for all (dp[i][k], dp[k+1][j]) for k in range [i,j] )        
		"""
        n = len(arr)
        dp = [[float('inf')] * n for _ in arr]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # to deal with even length palindrome as well, we pre fill for length 2
                if i == j or (arr[i] == arr[j] and j - i == 1 ):                              
                    dp[i][j] = 1
                    continue
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]     
                for k in range(i, j):
                    dp[i][j] = min( dp[i][j], dp[i][k] + dp[k+1][j] )
        return dp[0][n - 1]
      
      
------------------------------------------------------
"""
1246. Palindrome Removal


very similar to strange printer or things like burst-balloon

first we think about and assume the worst case, that every character is unique. 
no palindromic structure is found, so we would have to pay for each character.

that is handled by this line:
ret = dfs(left + 1, right) + 1

which turns the recursion tree into something like a linked list till 
it consumes the string.

now, every recursive step, we examine all characters that are left
in the string beteen left+1 and right (inclusive) and compare it against
the left, and we try to minimize the moves needed for subarrays (substrings),
which is what ret is capturing. this exploits the palindromic structure, but
there might be multiple potential optimal paths.

if there is a match between the current left and the proposed interval, 
this generates two subproblems that we continue recursion into.

there is an edge case here when there are two characters left:
 left_ret = max(1, dfs(left+1, mid - 1))

Complexity:
O(N^3) time, O(N^2) space
"""
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:

        @cache
        def dfs(left, right):
            
            if left > right:
                return 0
            
            ret = dfs(left + 1, right) + 1
            

            for mid in range(left+1, right+1): 
                if arr[mid] == arr[left]:
                    left_ret = max(1, dfs(left+1, mid - 1))
                    right_ret = dfs(mid + 1, right)
                    
                    ret = min(ret, left_ret + right_ret))

            return ret

        arr = arr
        return dfs(0, len(arr) - 1)
		```
    
--------------------------------------------------------------------------------
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        if not arr or not arr[0]:
            return 0
        dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)-1,-1,-1):
            for j in range(i,len(arr)):
                if i == j:
                    dp[i][j] = 1
                elif i+1 == j:
                    if arr[i] == arr[j]: # case : 121 131
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 2 # case: 123
                else:
                    dp[i][j] = min(dp[i][j-1]+1,dp[i+1][j]+1,dp[i+1][j-1] + (0 if arr[i] == arr[j] else 2))
                    #   case : 11112,21111    12221 or 12223
                    for k in range(i,j):
                        dp[i][j] = min(dp[i][k]+dp[k+1][j],dp[i][j])
        return dp[0][-1]
