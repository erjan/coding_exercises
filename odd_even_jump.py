'''
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.
'''

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
		# find next index of current index that is the least larger/smaller
        def getNextIndex(sortedIdx):
            stack = []
            result = [None] * len(sortedIdx)
        
            for i in sortedIdx:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        sortedIdx = sorted(range(len(A)), key= lambda x: A[x])
        oddIndexes = getNextIndex(sortedIdx)
        sortedIdx.sort(key=lambda x: -A[x])
        evenIndexes = getNextIndex(sortedIdx)
        
		# [odd, even], the 0th jump is even
        dp = [[0,1] for _ in range(len(A))]
        
        for i in range(len(A)):
            if oddIndexes[i] is not None:
                dp[oddIndexes[i]][0] += dp[i][1]
            if evenIndexes[i] is not None:
                dp[evenIndexes[i]][1] += dp[i][0]
				
        return dp[-1][0] + dp[-1][1]
      
-----------------------------------------------------------------------------------------------------------
# Time : O(n^3)
# Space : O(1)
# class Solution:
#     def oddEvenJumps(self, arr : List[int]) -> int:
#         good_jump = 0
#         for i in range(len(arr)):
#             j = i + 1
#             k = i 
#             cnt = 1
#             while j < len(arr):
#                 if cnt % 2 == 0:
#                     k = self.searchEven(k, j, arr)
#                 else:
#                     k = self.searchOdd(k, j, arr)
                
#                 cnt += 1
#                 j = k + 1

#                 if k == -1:
#                     break
#             if j == len(arr):
#                 good_jump += 1
#         return good_jump
    
#     def searchOdd(self, k, j, arr):
#         smallest = float("inf")
#         smallest_idx = -1
#         while j < len(arr):
#             if arr[k] <= arr[j]:
#                 if arr[j] < smallest:
#                     smallest = arr[j]
#                     smallest_idx = j
#             j += 1
#         return smallest_idx
    
#     def searchEven(self, k, j, arr):
#         largest = float("-inf")
#         smallest_idx = -1
#         while j < len(arr):
#             if arr[k] >= arr[j]:
#                 if arr[j] > largest:
#                     largest = arr[j]
#                     smallest_idx = j
#             j += 1
#         return smallest_idx

# sol = Solution()
# arr = [10, 13, 12, 14, 15]
# arr = [2, 3, 1, 1, 4]
# arr = [5, 1, 3, 4, 2]
# print(sol.oddEvenJumps(arr))

# ------------------------ Solution - 2 (optimized)

# Time : O(nlog(n))
# Space : O(n)

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        # ---- Find the next odd jump indices

        odd_jump_idx = [0] * len(arr)
        stack = []
        first = False
        for idx, val in sorted(enumerate(arr), key = lambda x : x[1]):
            if not first:
                stack.append(idx)
                first = True
                continue
            while len(stack) and stack[-1] < idx:
                odd_jump_idx[stack.pop()] = idx
            stack.append(idx)
        
        # ---- Find the next even jump indices
        
        even_jump_idx = [0] * len(arr)
        stack = []
        first = False
        for idx, val in sorted(enumerate(arr), key = lambda x : x[1], reverse = True):
            if not first:
                stack.append(idx)
                first = True
                continue
            while len(stack) and stack[-1] < idx:
                even_jump_idx[stack.pop()] = idx
            stack.append(idx)

        odd_start_good = [0] * len(arr)
        even_start_good = [0] * len(arr)

        # --- Use the above jump indices arrays to find if each index can odd-start and even-start
        # --- jump to position n - 1

        # Base Case : the last index can always reach itself.
        odd_start_good[len(arr) - 1] = 1 # 1 = can reach n-1 and 0 otherwise
        even_start_good[len(arr) - 1] = 1 # 1 = can reach n-1 and 0 otherwise

        for idx in reversed(range(len(arr) - 1)):
            idx_next_odd = odd_jump_idx[idx]
            if idx_next_odd and even_start_good[idx_next_odd]: # if idx_next_odd and even_start_good both are any values > 0
                odd_start_good[idx] = 1 # then it index is good to start with odd jump and reach the end.

            idx_next_even = even_jump_idx[idx]
            if idx_next_even and odd_start_good[idx_next_even]:
                even_start_good[idx] = 1
            
        # -- The sum of odd_start_good is equal to the number of good indices.

        return sum(odd_start_good)
        
