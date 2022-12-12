'''
You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.

We define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).

Return the K-Sum of the array.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Note that the empty subsequence is considered to have a sum of 0.
'''

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap = [(-maxSum + absNums[0], 0)]
        ans = [maxSum]
        while len(ans) < k:
            nextSum, i = heapq.heappop(maxHeap)
            heapq.heappush(ans, -nextSum)
            if i + 1 < len(absNums):
                heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return ans[0]
      
------------------------------------------------------------------------------------------------

'''
Intuition
Here, I will discuss a strategy to find the kth largest subsequence sum.

We start from the sum of all positive numbers in nums which is the largest one (say m);
To proceed, we subtract absolute values from m;
If the number is positive, this is equivalent to removing the number from the subsequence sum;
If the number is negative, this is equivalent to adding the number to the subsequence sum;
To enumerate all possitibilites, we generate a tree-ish path to cover different combinations;
This can be done by repeatedly generating two branches at each point with one always include a value at a given index i and the other always exclude the value.
Here, I use a priority queue to control for the size so that the runtime won't explode.
'''

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        m = sum(x for x in nums if x > 0)
        pq = [(-m, 0)] 
        vals = sorted(abs(x) for x in nums)
        for _ in range(k): 
            x, i = heappop(pq)
            if i < len(vals): 
                heappush(pq, (x+vals[i], i+1))
                if i: heappush(pq, (x-vals[i-1]+vals[i], i+1))
        return -x
