'''
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.
'''
#my thoughts - draft(not working)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def helper(nums, l,r,val,diff):

            for i in range(l,r+1):
                if abs(val- nums[i]) >=0:
                    nums[i] = 0
                else:
                    nums[i] = nums[i]-val
            
            #check if nums[i] is zero array
            if nums == [0]*len(nums):
                return 1
            return -1


        queries = [ [l,r,val, r-l] for l,r, val in queries ]
        k = float('inf')
        for i, val_ in enumerate(queries):
            l,r,val, diff = val_
            temp = helper(nums, l,r,val,diff)
            k = min(k, i)

        
        if k == float('inf'):
            return -1
        return k
--------------------------------------------------
#from editorial

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True
