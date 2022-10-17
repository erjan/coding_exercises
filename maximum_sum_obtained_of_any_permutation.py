'''
We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

Return the maximum total sum of all requests among all permutations of nums.

Since the answer may be too large, return it modulo 109 + 7.
'''

'''
Intuition
We want to calculate the frequency for A[i].
Assign the big element A[i] to the position queried more frequently.


Explanation
For each request [i,j],
we set count[i]++ and count[j + 1]--,

Then we sweep once the whole count,
we can find the frequency for count[i].

Note that for all intervals inputs,
this method should be the first intuition you come up with.

Main idea: Count the frequency with which each index appears in requests array. Then sort frequency and nums arrays and pair them. Thus, the largest value in nums array have to be paired with the highest frequency value.

Main difficulty is to count frquencies. The naive implementation may result in TLE. Thus, we have to come up with something smart.

Improved algorithm:

Lets create array freq with size n + 1
Loop through requests array:
Let say there is some a,b = requests[i].
Increment freq[a] and decrement freq[b+1].
Loop over freq array and accumulate frequencies:
freq[i] += freq[i-1]
The correctness of the algorithm is quite intuitive.
M is the size of requests array and N is size of nums array.

Time complexity: O(M + NlogN)
Space complexity: O(N)
'''

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0
        freq = [0] * (n+1)
        for (a,b) in requests:
            freq[a] += 1
            freq[b + 1] -= 1
        for i in range(1,len(freq)):
            freq[i] += freq[i-1]
        freq.sort(reverse = True)
        nums.sort(reverse = True)
        return sum([freq[i]*nums[i] for i in range(n)])%MOD
      

def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        t = [0]*(n + 1)
        for a, b in requests:
            t[a] += 1
            t[b + 1] -= 1
        for i in range(1, n):
            t[i] += t[i - 1]
        
        nums.sort()
        t.pop()
        t.sort()

        return sum(a*b for a, b in zip(nums, t)) % mod
      
---------------------------------------------------------------------------------------------      
