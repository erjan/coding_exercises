'''
You are currently designing a dynamic array. You are given a 0-indexed integer array nums, where nums[i] is the number of elements that will be in the array at time i. In addition, you are given an integer k, the maximum number of times you can resize the array (to any size).

The size of the array at time t, sizet, must be at least nums[t] because there needs to be enough space in the array to hold all the elements. The space wasted at time t is defined as sizet - nums[t], and the total space wasted is the sum of the space wasted across every time t where 0 <= t < nums.length.

Return the minimum total space wasted if you can resize the array at most k times.

Note: The array can have any size at the start and does not count towards the number of resizing operations.
'''

'''
1) keywords for identifying it as DP:
at most 'k' operations
minimize the space wasted

2) for state identification: 
If we increase or decrease 'k', will it affect our answer? "Yes", hence this is a state. 
If we change size of "nums" will it affect our answer? "Yes", hence index is a state too.
Is there anything else which can contribute in answer? "I don't feel so", hence there are only two states.

3) for base cases:
Base case for state "index": if 'index' == 'sizeof(nums)', no space is wasted, return 0.
Base case for state "k": if 'k'<'0', that means we have overused 'k' hence return 'INT_MAX'.

4) for state transformation:
At any [idx,k], we have two options, either change value here or don't change here.
But if we change value, what value we will update with?
This is the core of problem, let's suppose we decide that we will update value at next 'index' == 'j', so the value we upadte with must be greater than all values from 'index i to j'.
What will be wasted space for that case?
max_element in 'i to j' * (j-i+1) - sum[i...j] + solve(j+1,k-1)
I know previous line is hard to understand, give it some though.
'''

class Solution:
    def minSpaceWastedKResizing(self, A: List[int], K: int) -> int:
        def waste(i, j, h):
            sumI = sums[i-1] if i > 0 else 0
            return (j-i+1)*h - sums[j] + sumI
        
        def dp(i, k):
            if i <= k:
                return 0
            if k < 0:
                return MAX
            if (i, k) in memoize:
                return memoize[(i, k)]
            
            _max = A[i]
            r = MAX
            for j in range(i-1, -2, -1):
                r = min(r, dp(j, k-1) + waste(j+1, i,  _max))
                _max = max(_max, A[j])

            memoize[(i, k)] = r
            return r
        
        sums = list(accumulate(A))
        n = len(A)
        MAX = 10**6*200
        memoize = {}

        return dp(n-1, K)
      
--------------------------------------------------------------------------------------------------------------------------------
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
		#I recomment using C++ or Java because even the optimised solution in python can be TLE
        
        #the idea here is to split nums into k+1 subarrays, and split it in such way that minSpaceWasted
        #u can think of max integer in a split to be a representation of that split
        #if k = 1, then first split was decided at initial val (doesnt count towards k), and resizing happens at the start of second split
        #which means the only uniqe state parameters are idx (idx represents nums[idx:]) and k (number of splits left to make)
        n = len(nums)
        @cache
        def makeSplits(i, k):
            if n-i <= k+1: return 0
            if k < 0: return math.inf
            
            res = math.inf
            c_max = c_sum = 0
            #j represents the end of c_split
            for j in range(i, n):
                c_max = max(nums[j], c_max)
                c_sum += nums[j]
                wasted = c_max*(j - i + 1) - c_sum
                res = min(res, makeSplits(j+1, k-1) + wasted)
            
            return res
        # Time -> O(n*k *n), Space -> O(n*k)
        # even with cache its a bit too slow and sometimes get rejected
        return makeSplits(0, k)
        
        #More space efficient solution and using iteration
        #Space -> O(n)
        res = [] #res[i] represents minWasted solution for nums[:i+1]
        c_max = c_sum = 0
        for i in range(n):
            c_max = max(c_max, nums[i])
            c_sum += nums[i]
            res.append((i+1)*c_max - c_sum)
        
        for resize in range(1, k+1):
            for i in range(n-1, -1, -1):
                c_sum = c_max = 0
                #j represents the start of a new split
                for j in range(i, 0, -1):
                    c_sum += nums[j]
                    c_max = max(c_max, nums[j])
                    res[i] = min(res[i], res[j-1] + (i - j + 1)*c_max - c_sum)
        
        return res[-1]
