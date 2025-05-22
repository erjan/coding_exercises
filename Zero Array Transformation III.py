You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
  ----------------------------------------
  class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)

        avail = []   # max‐heap of ends (store negatives)
        active = []  # min‐heap of ends
        chosen = 0
        for i in range(n):
            for r in starts[i]:
                heapq.heappush(avail, -r)

            while active and active[0] < i:
                heapq.heappop(active)

            need = nums[i] - len(active)
            for _ in range(need):
                while avail and -avail[0] < i:
                    heapq.heappop(avail)
                if not avail:
                    return -1
                r = -heapq.heappop(avail)
                heapq.heappush(active, r)
                chosen += 1
        return q - chosen
