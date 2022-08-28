'''
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()

        pref = list()
        pref.append(nums[0])

        for i in range(1, len(nums)):
            pref.append(pref[i-1] + nums[i])
        ans = [0] * len(queries)
        for i in range(len(queries)):
            cur_sum = 0
            query = queries[i]
            ind = -1
            for j in range(len(nums)):
                if cur_sum + nums[j] > query:
                    break
                cur_sum = cur_sum + nums[j]
                ind = j
            ans[i] = ind+1
        return ans
