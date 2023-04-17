'''
You are given two 0-indexed integer arrays nums and divisors.

The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

Return the integer divisors[i] with the maximum divisibility score. If there is more than one integer with the maximum score, return the minimum of them.
'''



class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        res = []

        for d in divisors:
            count = 0
            for n in nums:

                if n % d == 0:
                    count += 1

            res.append([d, count])

        m = [(x[1]) for x in res]
        m = max(m)
        final = sys.maxsize

        for a, b in res:
            if b == m:
                final = min(final, a)

        return final
      
----------------------------------------------------------------------------------------
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        l=[]
        divisors.sort()
        for i in divisors:
            c=0
            for j in nums:
                if j%i==0:
                    c+=1
            l.append(c)
        return divisors[l.index(max(l))]
            
