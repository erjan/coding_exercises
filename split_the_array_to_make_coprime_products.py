'''
You are given a 0-indexed integer array nums of length n.

A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.

For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
Return the smallest index i at which the array can be split validly or -1 if there is no such split.

Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.

 
 '''




'''
Intuition
If arr[0]==2, and if no factor "2" in the rest of the array, then arr[0] is the split point. If arr[5] also has prime factor "2", then it is not possible to split at arr[0~4]. The split index must be >=5. Also if all prime factors in arr[0~5] doesn't exist after arr[5], then the split point is arr[5], otherwise the split index is >5.

Approach
We record the right-most index of each prime factor into a dictionary. Then start from arr[0], we keep updating the right-most index scanned so far. If the current right-most index is "i" itself, then that means "i" is the smallest splitting point.
'''

mx = 10**6
spf = [i for i in range(mx+1)]
for i in range(2,int(math.sqrt(mx))+1):
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=min(spf[j],i)
def getPrimeFactors(x):
    while x!=1:
        yield spf[x]
        x//=spf[x]
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        fac_idx = defaultdict(int)
        for i,v in enumerate(nums):
            for fac in getPrimeFactors(v):
                fac_idx[fac] = i
        right_most = 0
        for i in range(len(nums)-1):
            for fac in getPrimeFactors(nums[i]):
                right_most = max(right_most,fac_idx[fac])
            if right_most==i:
                return i
        return -1
      
----------------------------------------------------------------------------------------
Intuition
Here, we cannot actually compute the products as they can become astronomically large. Rather, we can collect prime factors and check if at any index no common prime factors were found in the prefix and suffix arrays.
Implementation

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        freq = Counter()
        for x in nums: 
            for p in range(2, isqrt(x)+1): 
                while x % p == 0: 
                    freq[p] += 1
                    x //= p 
            if x > 1: freq[x] += 1
        ovlp = 0 
        prefix = Counter()
        for i, x in enumerate(nums): 
            if i <= len(nums)-2: 
                for p in range(2, isqrt(x)+1): 
                    if x % p == 0: 
                        if prefix[p] == 0: ovlp += 1
                        while x % p == 0: 
                            prefix[p] += 1
                            x //= p 
                        if prefix[p] == freq[p]: ovlp -= 1
                if x > 1: 
                    if prefix[x] == 0: ovlp += 1
                    prefix[x] += 1
                    if prefix[x] == freq[x]: ovlp -= 1
                if not ovlp: return i 
        return -1 
