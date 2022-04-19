'''
You are given a binary array nums containing only the integers 0 and 1. Return the 
number of subarrays in nums that have more 1's than 0's. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous sequence of elements within an array.
'''


change zeros in nums to minus ones and do prefix sum on nums. this way, if prefix[i+k] > prefix[i], that means subsequence nums[i+1] to nums[k] (both sides inclusive) have more ones than zeros. we iterate through the list of prefix sums, and keep book of counts for each prefix value. At i, number of subsequences that ends at i and starts at any j that j <= i are number of counts of prefix sums whose values are < prefix[i]

a straightfoward O(n^2) solution:
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        nums = [i if i else -1 for i in nums]
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        
        cnt = Counter()
        res = 0
        mod = 1000000007
        for i in range(n+1):
            cnt[presum[i]] += 1 
            res += sum([v for k, v in cnt.items() if k < presum[i]]) % mod
        return res % mod
Binary Indexed Tree
in the solution above, in each iteration, there's at most O(n) operations to get sums of all counts whose values are below current prefix sum. one way to fasten this is to use Binary Indexed Tree that supports O(logn) value update, and O(logn) range sum. Use this on prefix sum counter. the overall run time is O(nlogn)

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        
        def addOne(k):
            while k <= cap:
                cnt[k] += 1
                k += k & -k
        
        def rangeSum(k, res):
            while k:
                res += cnt[k]
                k -= k & -k
            return res % mod
        
        nums = [0] + [i if i else -1 for i in nums]
        n, cap, bot = len(nums), 0, 0
        for i in range(1, n):
            nums[i] += nums[i-1]
            if nums[i] < bot: bot = nums[i]
            if nums[i] > cap: cap = nums[i]
        
        add = -bot + 1   # parallel shifting presums to make smallest presum (i.e. first index) start at 1
        cap += add
        cnt, res, mod = Counter(), 0, int(10**9+7)
        for i in range(n):
            k = nums[i] + add
            addOne(k)
            res = rangeSum(k-1, res)
            
        return res % mod
O(n) solution
notice prefix[i] = either prefix[i-1] + 1 or prefix[i-1] - 1,

if prefix[i] = prefix[i-1] + 1: current number of qualified sequences are previous sum of count of prefixes thats < prefix[i-1] (book this) + count of prefix[i-1].
if prefix[i] = prefix[i-1] - 1: current number of qualified sequences are previous sum of count of prefixes thats < prefix[i-1] (book this) - count of prefix[i-1] - 1
this shortcut makes O(1) in each iteration. So overall run time is O(n)

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        nums = [0] + [i if i == 1 else -1 for i in nums]
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        cnt = Counter()
        res, pre, precnt, mod = 0, 0, 0, int(10**9+7)
        for cur in nums:
            if cur == pre + 1:
                precnt += cnt[pre] % mod
            else:  # cur == pre - 1
                precnt -= cnt[pre-1] % mod
            res += precnt
            cnt[cur] += 1
            pre = cur
            
        return res % mod
------------------------------------------------------------------------------
Time O(N)
Space O(N)

Let say the number of 1 in a subarray is ones and 0 is zeros. We can calculate (ones - zeros) of nums[:i+1] for each position i through the array nums and store them in an array diffs.

At each position i we know that the difference at j where j < i and diffs[j] < diffs[i] guarantees that nums[j+1:i+1] is a good subarray which is ones > zeros.

In addition, we also know diffs[i] == diffs[i - 1]) +/- 1. Let say dp[i]is the number of good substrings with the end of nums[i], we know that

if nums[i] == 1 , then diffs[i] == diffs[i - 1] + 1, and dp[i] = dp[i - 1] + (the number of j, where j < i and diffs[j] == nums[i - 1].
if nums[i] == 0 , then diffs[i] == diffs[i - 1] - 1, and dp[i] = dp[i - 1] - (the number of j, where j < i and diffs[j] == nums[i - 1] - 1.
If we maintain a dictionary countsthrough the iteration, then we can simply get the plus/minus between dp[i] and dp[i - 1]. Here is my code:

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10** 9 + 7
        counts = collections.Counter({0:1})
        res = s = dp = 0
        for n in nums:
            if n:
                s += 1
                dp += counts[s - 1]
            else:
                s -= 1
                dp -= counts[s]
            res = (res + dp) % MOD
            counts[s] += 1
        
        return res % MOD
--------------------------------------------------------------
                                                                              class BinaryIndexedTree:
    
    def __init__(self, n):
        self._len = n + 1
        self._BIT = [0] * self._len
    
    
    def query(self, index):
        index += 1
        ret = 0
        while index:
            ret += self._BIT[index]
            index -= (index & -index)
            
        return ret
        
    
    def add(self, index, delta):
        index += 1
        while index < self._len:
            self._BIT[index] += delta
            index += (index & -index)
        
        
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + n * 2 - 1
            
        MIN, MAX = min(prefix_sum), max(prefix_sum)
        bit = BinaryIndexTree(MAX - MIN + 1) 
            
        ret = 0
        for p in prefix_sum:
            ret += bit.query(p - MIN - 1)
            
            bit.add(p - MIN, 1)
            
        return ret % (10 ** 9 + 7)
------------------------------------------------------------------------------------------------
                                                                              Initialization Step

We initialize 2 stacks:

A stack called negatives to store the count of subarrays with more zeros than ones such that negatives[-k] is the count of subarray with exactly k more zeroes than ones
A stack called positives to store the count of subarrays with less zeros than ones such that positives[-k] is the count of subarray with exactly k less zeroes than ones
Also 2 integers:

An integer called zeroes to store the acount of subarrays with equal zeroes than ones
An integer called total_sum to track the total number of valid subarrays
Iteration Step

For each iteration i:

If nums[i] == 0:
Push zeroes + 1 to negatives (all subarrays with equal zeroes than ones become negative + the subarray 0)
Then pop positives and store it into zeroes (all subarrays with exactly one less zeroes than ones now belong in zeroes)
If nums[i] == 1
Push zeroes + 1 to positives (all subarrays with equal zeroes than ones become positive + the subarray 1)
Then pop negatives and store it into zeroes (all subarrays with exactly one more zeroes than ones now belong in zeroes)
Then we add sum(positives) into total_sum
That's it! We're done!

Well, almost, we want to optimize the step where we do sum(positives) on each iteration. So we'll just cache sum(positive) into a variable called positive_sum.

It's better to show than tell:

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        negatives, zeroes, positives = [], 0, []
        
        total_sum, positives_sum = 0, 0
        for num in nums:
            if num == 0:
                negatives.append(zeroes + 1)
                zeroes = positives.pop() if positives else 0
                positives_sum -= zeroes
            else:
                positives.append(zeroes + 1)
                zeroes = negatives.pop() if negatives else 0
                positives_sum += positives[-1]

            total_sum += positives_sum

        return total_sum % (10 ** 9 + 7)
                                                                              
                                                                              
---------------------------------------------------------------------------------------------
                                                                              Ideas
Replace every occurrence of 0 with -1
Compute the prefix sum. Observe that -1 (s) will cancel out 1 (s).
The prefix sum value at any index i < N can be negative, zero, or positive. The first case happens when there are more zeros than ones while the last case occurs when the opposite happens. The second case happens when there's an equilibrium of zeros and ones.
Positive prefix sum value contributes 1 valid subarray
Each of the previous prefix sum values from [0: i-1] that is smaller than the current prefix sum value contributes 1 valid subarray
Solution
import sortedcontainers

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        cands = sortedcontainers.SortedList()
        acc = ans = 0
        mod = 10**9 + 7
        for num in nums:
            acc += 1 if num else -1
            
            idx = cands.bisect_left(acc)
            ans = (int(acc > 0) + ans + idx) % mod
            cands.add(acc)
        return ans
Complexity
Time: O(NlogN) . Each iteration uses 2 logN operations, there are N such iterations
Space: O(N) for the prefix sum array
                                                                              
                                                                              
      
