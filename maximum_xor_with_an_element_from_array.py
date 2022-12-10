'''
You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
'''

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        ans = [-1]*len(queries)
        
        trie = {}
        k = 0
        for m, x, i in queries: 
            while k < len(nums) and nums[k] <= m: 
                node = trie
                val = bin(nums[k])[2:].zfill(32)
                for c in val: node = node.setdefault(int(c), {})
                node["#"] = nums[k]
                k += 1
            if trie: 
                node = trie
                val = bin(x)[2:].zfill(32)
                for c in val: node = node.get(1-int(c)) or node.get(int(c))
                ans[i] = x ^ node["#"]
        return ans 
