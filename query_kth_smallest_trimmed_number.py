'''
You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

Trim each number in nums to its rightmost trimi digits.
Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
Reset each number in nums to its original length.
Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.

Note:

To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
Strings in nums may contain leading zeros.
'''


from collections import defaultdict

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        sl = len(nums[0])
        len_to_sorted = defaultdict(list)
        ans = [0] * len(queries)
        
        for i, (k_smallest, trim_len) in enumerate(queries):
            if trim_len not in len_to_sorted:
                # have to trim
                for ni, num in enumerate(nums):
                    len_to_sorted[trim_len].append( (int(num[sl - trim_len:]), ni) )
					
                len_to_sorted[trim_len] = sorted(len_to_sorted[trim_len])
            ans[i] = len_to_sorted[trim_len][k_smallest -1][1]
            
            
        return ans
