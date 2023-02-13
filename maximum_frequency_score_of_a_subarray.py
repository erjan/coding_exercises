'''
You are given an integer array nums and a positive integer k.

The frequency score of an array is the sum of the distinct values in the array raised to 
the power of their frequencies, taking the sum modulo 109 + 7.

For example, the frequency score of the array [5,4,5,7,4,4] is (43 + 52 + 71) modulo (109 + 7) = 96.
Return the maximum frequency score of a subarray of size k in nums. You should maximize the 
value under the modulo and not the actual value.

A subarray is a contiguous part of an array.
'''



Since the score is defined under modulo, we need to literally follow the description to use a length-k sliding window computing scores and take the max.

A simple window frequency counter and recompute all scores within the window will result in TLE. In fact, we only need to compute all for the initial window at index 0, then every step forward, there is only one left value moves out of the window, and one right element enters the window. I.e., at most, there are two values' (may be none if left == right) frequencies changing.

Example:
[2,1,2,3,1], k = 3
i = 0, ct = {1: 1, 2: 2}, score = 5;
i = 1, ct = {1: 1, 2: 1, 3: 1}, score = 5 - 2^2 + 2^1 + 3^1 = 6;
i = 2, ct = {1: 1, 2: 1, 3: 1}, left = right, no change in score;
max = 6.

Note i = 1 when 3 enters the window, the window at i = 0 has no 3 in it, we must not substract 3^0 = 1 from score.

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        @cache
        def modpow(v, x):
            return pow(v, x, MOD)

        n = len(nums)
        MOD = 1_000_000_007
        ct = Counter(nums[:k])
        cur = 0
        for v in ct:
            cur = (cur + modpow(v, ct[v])) % MOD
        ans = cur

        for i in range(1, n - k + 1):
            le = nums[i - 1]
            ri = nums[i + k - 1]
            # same value in and out, skipping
            if le == ri: 
                continue
            #
            # left end out of the window
            cur -= modpow(le, ct[le])
            if ct[le] > 1: # do not include le^0
                cur += modpow(le, ct[le] - 1)
            #
            # right end into the window
            if ct[ri]: # do not substract ri^0
                cur -= modpow(ri, ct[ri])
            cur += modpow(ri, ct[ri] + 1)
            cur %= MOD
            #
            # update answer and ct
            ans = max(cur, ans)
            ct[le] -= 1
            if not ct[le]:
                del ct[le]
            ct[ri] += 1
        return ans
