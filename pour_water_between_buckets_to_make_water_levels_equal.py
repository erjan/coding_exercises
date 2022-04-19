'''
You have n buckets each containing some gallons of water in it, represented by a 0-indexed integer array buckets, where the ith bucket contains buckets[i] gallons of water. You are also given an integer loss.

You want to make the amount of water in each bucket equal. You can pour any amount of water from one bucket to another bucket (not necessarily an integer). However, every time you pour k gallons of water, you spill loss percent of k.

Return the maximum amount of water in each bucket after making the amount of water equal. Answers within 10-5 of the actual answer will be accepted.
'''

Explanation
The idea is same as implement double sqrt(double n) using binary search. Below is a template.
def sqrt_double(x):
	left, right = (1, x) if x >= 1 else (x, 1)
	while right - left >= 1e-10:     # precision is 1e-10
		mid = left + (right - left) / 2
		if mid * mid <= x:
			left = mid
		else:
			right = mid
	return right  
See comments below for more explanation
Implementation
class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        l, r = min(buckets), sum(buckets) / len(buckets) # initialize lowest and highest possible value
        left_over = 1-loss/100                           # calculate left over ratio
        def ok(val):                                     # check if reach to an average of `val` is posible
            cnt = 0
            for bucket in buckets:
                if bucket >= val:
                    cnt += (bucket - val) * left_over    # count left_over after pouring water
                else:
                    cnt -= (val - bucket)                # reduce count for those bucket need more water to reach `val`
            return cnt >= 0
        while r - l >= 1e-5:                             # by description, epsilon is 1e-5
            mid = (l + r) / 2                            # binary search
            if ok(mid):
                l = mid 
            else:    
                r = mid 
        return r
--------------------------------------------------------------------------
We just need to check whether a final equal amount v works for our input. We check that by

asset = sum(x-v for x in buckets if v<x)
debt = sum(v-x for x in buckets if v>x)
if asset * k >= debt
And then we can just binary search to find out the largest v. That's when asset == debt, we increase the lo instead of decreasing the hi.
Be aware of that is a float binary search, we need to set up a machine precision epsilon to avoid the loop.

def equalizeWater(buckets, loss):
	lo, hi, eps, k = 0, max(buckets), 10**-5, (100-loss)/100
	while hi - lo > eps:
		v = (lo+hi)/2
		if sum(x-v for x in buckets if v<x)*k >= sum(v-x for x in buckets if v>x):
			lo = v
		else:
			hi = v
	return lo
-----------------------------------------------------------
We first sort buckets, then traverse from right to left so that we can early termination.
n - i buckets will pour out, while i buckets will be poured in.
Suppose x is the final amount. It is easy to derive to the formula.
Let pct = 1.0 - loss / 100.0
(right - (n - i) * x) * pct = i * x - left
x = (right * pct + left) / (pct * (n - i) + i)

    buckets.sort()
    
    if buckets[0] == buckets[-1]:
        return buckets[0]

    n = len(buckets)
    pct = 1.0 - loss / 100.0

    right = 0
    left = sum(buckets)
    for i in range(n - 1, 0, -1):
        right += buckets[i]
        left -= buckets[i]
        x = (right * pct + left) / (pct * (n - i) + i)
        if buckets[i - 1] <= x <= buckets[i]:
            return x

    return -1.0
  --------------------------------------------------------------------------------------------------
  To be honest, when I first look at this question, I had no idea. But the first hint is so subtle:

What is the range that the answer must fall into?

Then I realize, it must be binary search. But how though? I only knew we need to generate the answer from the range, but how do I adjust it for each round? Then I came up this solution where I compare the candidate answer with each existing bucket, and I can then calculate the total amount of water poured into the bucket or poured out of it. But we have loss here, so it is actually two different conditions:

If the bucket has more water than before, then (after - before) / (earn / 100) (Here earn = 100 - loss) amount of water was actually taken from other buckets
If the bucket has less water than before, then before - after amount of water was taken out of it
So we can sum up all the differences, and we expect it to be 0 as the water amount should be balanced in and out. If not, we can adjust our candidate answer based on it:

If more water is poured in than water taken out, then we know the candidate is too large, we need to reduce it
If less water is poured in thant water poured out, that's okay (we may waste some water by pouring A -> B -> C instead of A -> C directly), so we mark this as a potential answer and make the candidate larger
So here is the code:

class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        total_water = sum(buckets)
        size = len(buckets)
        if loss == 0: return total_water / size # if no loss, then we just get the average
        left, right = 0, max(buckets)
        epsilon = 0.00001 # 10^-5
        earn = 100 - loss
        def water_balance(average): 
            total = 0
            for water in buckets:
                if water < average:
                    total += (average - water) * 100 / earn
                else:
                    total -= water - average
            return total
            
        output = 0
        while right - left >= epsilon:
            mid = (left + right) / 2
            if size * mid > total_water or water_balance(mid) > 0: # condition 1
                right = mid
            else: # condition 2
                output = max(output, mid)
                left = mid
        return output
  

      
