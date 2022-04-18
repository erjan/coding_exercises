You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is greater than or equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


Let d(x, y) be the density of segment [x, y], ie. d(x, y) = (A[x]+...+A[y]) / (y-x+1). It can be computed quickly with prefix sums.

Now we refer to section 3 of Kai-min Chung, Hsueh-I Lu - An Optimal Algorithm for the Maximum-Density Segment Problem. 2008.

For each ending index j, the current interval for i under consideration, [0, j-K+1] (minus parts on the left we have already discarded), has been decomposed into minimum density segments of longest length [hull[i], hull[i+1]-1], and we discard these segments as appropriate. That is, for each i in increasing order, hull[i+1] is the largest index in [hull[i], j-K+1] so that [hull[i], hull[i+1]-1] has minimum density.

This is simply a lower hull of candidate points i, in a geometric interpretation where d(a, b) is the slope of the line segment (a, P[a]) to (b+1, P[b+1]). Then, we can prove that discarding components with lower density than our current candidate d(hull[0], j) must leave us with the highest density option remaining.

def findMaxAverage(self, A, K):
    N = len(A)
    P = [0]
    for x in A:
        P.append(P[-1] + x)

    def d(x, y):
        return (P[y+1] - P[x]) / float(y+1-x)

    hull = collections.deque()
    ans = float('-inf')

    for j in xrange(K-1, N):
        while len(hull) >= 2 and d(hull[-2], hull[-1]-1) >= d(hull[-2], j-K):
            hull.pop()
        hull.append(j-K + 1)
        while len(hull) >= 2 and d(hull[0], hull[1]-1) <= d(hull[0], j):
            hull.popleft()
        ans = max(ans, d(hull[0], j))

    return ans
  
---------------------------------------------------------------------------------------
Brute Force Solution

Simply call Maximum Average SubArray I in a look for all possible values of k.
Time Complexity is O(N^2).
class Solution:
    def get_max_average(self, nums, k):
        if len(nums) < k:
            return 0.0
        max_so_far = sum_so_far = sum(nums[:k])
        for i in range(k, len(nums)):
            sum_so_far = sum_so_far + nums[i] - nums[i-k]
            max_so_far = max(max_so_far, sum_so_far)
        return float(max_so_far)/k    
    
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = float('-inf')
        for x in range(k, len(nums)+1):
            result = max(result, self.get_max_average(nums, x))
        return result
Binary Search Solution

What is the range for the average value? Clearly, any average will lie between min(nums) and max(nums). So the intuition is to use binary search between this range.
lo is initialized to min(nums). hi is initialized to max(nums). x = mid = (lo+hi)/2
Now we want to solve the sub-problem: Does the array nums have a subarray of length greater than equal to k with average atleast x? If yes, then we can restrict our search to the range [x,hi]. Otherwise, we will search in the range [lo,x].
Can we devise a linear time solution for the problem: Does the array nums have a subarray of length greater than equal to k with average atleast x?
nums[i]+...+nums[j] >= x * (j-i-1). This evaluates to: (nums[i]-x) + (nums[i+1]-x) + ...(nums[j]-x) >=0
The problem is transformed into the following problem: Do we have a sub-array of length greater than k in the transformed array with sum greater than zero?
The above problem can be solved in linear time. Start by finding the sum of first k elements nums[i]-mid. If this sum is greater than zero, then we can return True. Otherwise, say we have the cumulative sum until index j i.e. cum(j) where j >= k. Now say we know the minimum cumulative sum until index i i.e. mcum(i) such that j-i >= k. Then if the cum(j) >= mcum(i), we can return True.
class Solution:
    def can_process(self, mid, nums, k):
        sum_so_far = 0
        for i in range(k):
            sum_so_far += nums[i] - mid
        if sum_so_far >= 0:
            return True
        prev, min_so_far = 0.0, 0.0
        for i in range(k, len(nums)):
            sum_so_far += nums[i] - mid
            prev += nums[i-k]-mid
            min_so_far = min(min_so_far, prev)
            if sum_so_far >= min_so_far:
                return True
        return False
    
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lo, hi = min(nums), max(nums)
        precision = 1E-6
        while hi-lo > precision:
            mid = lo + (hi-lo)/2.0
            if self.can_process(mid, nums, k):
                lo = mid
            else:
                hi = mid
        return lo
------------------------------------------------------------------------------------------------------
We binary search on the answer. Let P[i] = A[0] + A[1] + ... + A[i-1], the i-th prefix sum under A.

Let's focus our attention on possible(x), a function that is true iff it is possible to have an average of at least x. Consider the elements B = [a-x for a in A] with corresponding prefix sum Q[i] = P[i] - i*x under B.

We want to know if there is some >= K length subarray in B with average at least zero. Suppose the subarray is B[i] + B[i+1] + ... + B[j] = Q[j+1] - Q[i]. To check whether this quantity is positive, for any j, and any i <= j - K + 1, we should check whether Q[j+1] >= min_{i <= j-K+1} Q[i]. Keeping a running minimum m of this array Q, we can check this in linear time.

Unfortunately, the time constraint on Python solutions is fairly tight, so we need another trick to avoid TLE. If a segment has the biggest average and we break it into two pieces, one of its pieces also has at least the same average. When the length is >= 2*K, we can split it into pieces of at least length K, with the largest such piece being less than length 2*K.

Thus, we only need to check segments of length K <= L < 2*K to find an instance of the maximum average. When K is small, this admits an O(NK) solution that we use instead. Our solution in that case is identical to Maximum Average Subarray I, repeated K times.

def findMaxAverage(self, A, K):
    N = len(A)
    P = [0]
    for x in A:
        P.append(P[-1] + x)

    if K < 100:
        ans = float('-inf')
        for k in xrange(K, min(2*K, N+1)):
            best_sum = max(P[i+k] - P[i] for i in xrange(N-k+1))
            ans = max(ans, best_sum / float(k))
        return ans

    def possible(x):
        m = P[0]
        for i, v in enumerate(P):
            m = min(m, v-i*x)
            if i+K == len(P): break
            if P[i+K] - (i+K)*x >= m:
                return True
        return False

    lo, hi = min(A), max(A)
    while hi - lo > .00001:
        mi = (lo + hi) / 2.0
        if possible(mi):
            lo = mi
        else:
            hi = mi
    return lo
  ------------------------------------------------------------------------------------------
  Most important concept here is, given any array and an average window of "k", it is possible to find whether there exists a subarray whose average value is bigger than "x", and find it in O(n) time.
How to check whether an average bigger than "x" exists in O(n) time?

Minus all elements in the array by "x".
After that, if we see any subarray that has sum>=0 means the average of this subarray is bigger than "x"
To find subarray bigger than "0", we just scan the array and find biggest subarray so far.
We can use prefix sum to find subarray of any target value. Since we are looking for the biggest subarray, we only need to remember the smallest prefix sum before current. The current prefix sum minus the smallest prefix sum is the biggest subarray so far. And if such subarray is bigger than zero, we find the result.
With this very important algorithm, we can use binary search between the smallest and biggest average "value" of the array to find final result.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        def isbigger(target):
            cur=0
            for i in range(k):
                cur+=nums[i]-target
            if cur>=0:
                return True
            prev=0
            prevmin=0
            for i in range(k,n):
                cur+=nums[i]-target
                prev+=nums[i-k]-target
                prevmin=min(prevmin,prev)
                if cur>=prevmin:
                    return True
            return False
        i,j=min(nums),max(nums)
        while j-i>=0.000004:
            mid=(i+j)/2.0
            if isbigger(mid):
                i=mid
            else:
                j=mid
        return i
------------------------------------------------------------------------------
Just implementing the binary search solution using NumPy for brevity and efficiency. Gets accepted in about 260 ms, easily beating 100% in the current runtime distribution (where times range from 439 ms to 1892 ms).

import numpy as np

class Solution(object):
    def findMaxAverage(self, nums, k):
        lo, hi = min(nums), max(nums)
        nums = np.array([0] + nums)
        while hi - lo > 1e-5:
            mid = nums[0] = (lo + hi) / 2.
            sums = (nums - mid).cumsum()
            mins = np.minimum.accumulate(sums)
            if (sums[k:] - mins[:-k]).max() > 0:
                lo = mid
            else:
                hi = mid
        return lo
      
  
      
