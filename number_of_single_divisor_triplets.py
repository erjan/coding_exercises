
'''
You are given a 0-indexed array of positive integers nums. A triplet of three distinct indices (i, j, k) is called a single divisor triplet of nums if nums[i] + nums[j] + nums[k] is divisible by exactly one of nums[i], nums[j], or nums[k].

Return the number of single divisor triplets of nums.
 

Example 1:

Input: nums = [4,6,7,3,2]
Output: 12
Explanation:
The triplets (0, 3, 4), (0, 4, 3), (3, 0, 4), (3, 4, 0), (4, 0, 3), and (4, 3, 0) have the values of [4, 3, 2] (or a permutation of [4, 3, 2]).
4 + 3 + 2 = 9 which is only divisible by 3, so all such triplets are single divisor triplets.
The triplets (0, 2, 3), (0, 3, 2), (2, 0, 3), (2, 3, 0), (3, 0, 2), and (3, 2, 0) have the values of [4, 7, 3] (or a permutation of [4, 7, 3]).
4 + 7 + 3 = 14 which is only divisible by 7, so all such triplets are single divisor triplets.
There are 12 single divisor triplets in total.
Example 2:

Input: nums = [1,2,2]
Output: 6
Explanation:
The triplets (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), and (2, 1, 0) have the values of [1, 2, 2] (or a permutation of [1, 2, 2]).
1 + 2 + 2 = 5 which is only divisible by 1, so all such triplets are single divisor triplets.
There are 6 single divisor triplets in total.
Example 3:

Input: nums = [1,1,1]
Output: 0
Explanation:
There are no single divisor triplets.
Note that (0, 1, 2) is not a single divisor triplet because nums[0] + nums[1] + nums[2] = 3 and 3 is divisible by nums[0], nums[1], and nums[2].

'''



Explanation
Count frequency for each unique key, this takes O(N)
Use nested loop to find 3 different keys and check they are possible Single Divisor Triplets
Any 3 unique values will have 6 different permutations (6 = 3 * 2 * 1)
Thus ans += v1 * v2 * v3 * 6, where v1,v2,v2 are frequency of each value
This takes O(100 ^ 3)
Use nested loop to find 2 different keys and assume one key will be used twice
e.g. (1, 2, 2) -> sum = 5 this is a Single Divisor Triplets since only 1 can be divided by 5
Any n same values will have n * (n-1) permutations
The third number will have 3 possible insertion location
Before two same values: 1 2 2
Between two same values: 2 1 2
After two same values: 2 2 1
Thus ans += v1 * (v1-1) * v2 * 3
This takes O(100 ^ 2)
Return ans,
Total time complexity: O(N + 100^3 + 100^2), since N < 10^5, the maximum time is bounded at O(100^3) significance level
Implementation
class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        ans, items, n = 0, list(c.items()), len(c)
        for i1, (k1, v1) in enumerate(items):                       # 3 unique keys
            for i2, (k2, v2) in enumerate(items[i1+1:], i1+1):
                for i3, (k3, v3) in enumerate(items[i2+1:], i2+1):
                    cur = k1 + k2 + k3
                    a1 = 1 - (cur % k1 == 0)
                    a2 = 1 - (cur % k2 == 0)
                    a3 = 1 - (cur % k3 == 0)
                    if a1 + a2 + a3 == 2:
                        ans += v1 * v2 * v3 * 6
        for i1, (k1, v1) in enumerate(items):                       # 2 unique keys, one key will be used twice
            if v1 == 1: continue
            for i2, (k2, v2) in enumerate(items):
                if i1 == i2: continue
                cur = 2 * k1 + k2
                if cur % k1 and cur % k2 == 0:
                    ans += v1 * (v1-1) * v2 * 3
        return ans
      
----------------------------------------------------------
The basic idea of this algorithm is brute force. Since the problem has given any number in nums is 1 <= num <= 100, then we can use 3 nested loops to find num[i], num[j], and num[k]. We can then get the sum and calculate if the condition is met.

For the purpose of checking if num[i], num[j], and num[k] are allowed, we can count the frequency before loops, then check inside loops. The frequency will also be used later to get our answer.

So, for example, if we have 3 numbers a, b, c that satisfy the condition, we can easily get one of the answer be (index(a), index(b), index(c)). By permutating it, we can have 6 more answers (permutation(3)). And for each number, it may have multiple indices. So overall, for each pair we find, we can have 6 * frequency[a] * frequency[b] * frequency[c] cases.

If two or three numbers are the same, we can change the fomula above using combinations, which is simple and straightforward and I won't explain further.

class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        from collections import Counter
        from math import comb
        freq = Counter(nums)
        res = 0
        for num_i in range(1, 101):
            if freq[num_i] <= 0: continue
            for num_j in range(num_i, 101):
                if freq[num_j] <= (num_i == num_j): continue
                for num_k in range(num_j, 101):
                    if freq[num_k] <= (num_k == num_i) + (num_k == num_j):
                        continue
                    sum_val = num_i + num_j + num_k
                    if (sum_val % num_i == 0 and sum_val % num_j != 0 and sum_val % num_k != 0)\
                    or (sum_val % num_j == 0 and sum_val % num_i != 0 and sum_val % num_k != 0)\
                    or (sum_val % num_k == 0 and sum_val % num_j != 0 and sum_val % num_i != 0):
                        if num_i == num_j == num_k:
                            res += 6 * comb(freq[num_i], 3)
                        elif num_i == num_j:
                            res += 6 * comb(freq[num_i], 2) * freq[num_k]
                        elif num_i == num_k:
                            res += 6 * comb(freq[num_i], 2) * freq[num_j]
                        elif num_j == num_k:
                            res += 6 * comb(freq[num_j], 2) * freq[num_i]
                        else: 
                            res += 6 * freq[num_i] * freq[num_j] * freq[num_k]
        return res
-----------------------------------------------------------------------------------
lass Solution:
    def valid_triplet(self, i, j, k):
        s = i + j + k
        if s % i == 0: return s % j != 0 and s % k != 0
        if s % j == 0: return s % k != 0        
        return s % k == 0
        
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        result, count = 0, Counter(nums)                    
        
        for i in range(1, 101):
            for j in range(i, 101):
                for k in range(j, 101):
                    if count[i] and count[j] and count[k] and self.valid_triplet(i, j, k):
                        if i == j:
                            result += count[i] * (count[i] - 1) // 2 * count[k]
                        elif j == k:
                            result += count[j] * (count[j] - 1) // 2 * count[i]                             
                        else:
                            result += count[i] * count[j] * count[k]
                                                        
        return 6 * result
---------------------------------------------------------------------------------------
Idea
find all single divisor value triplets (a, b, c) such that a <= b <= c.
the range of values is way smaller than the size of the array
for each single divisor value triplet (a, b, c), the answer will be increased by
freq[a] * freq[b] * freq[c] if a, b, c are distinct
C(freq[b], 2) * freq[c] if a == b
C(freq[b], 2) * freq[a] if b == c
notice it's not possible that a == b == c.
finally, multiply the answer by 3! = 6
since the required tuples are permutations.
----------------------------------------------------------------------------------------
class Solution:
def singleDivisorTriplet(self, nums: List[int]) -> int:
    def is_single_divisor_triplet(i, j, k):
		s = i + j + k
        if s % i == 0: return s % j != 0 and s % k != 0
        if s % j == 0: return s % k != 0
        return s % k == 0
    
    tuples = []
    for i in range(1, 101):
        for j in range(i, 101):
            for k in range(j, 101):
                if is_single_divisor_triplet(i, j, k):
                    tuples.append((i, j, k))
    
    occ = Counter(nums)
    
    def count_of_triplets(i, j, k):
        if i == j or j == k:
            return occ[j] * (occ[j] - 1) // 2 * occ[i if j == k else k]
        return occ[i] * occ[j] * occ[k]
        
    return 6 * sum([count_of_triplets(*tup) for tup in tuples])
we can also change the nested loop into list comprehension.
class Solution:
def singleDivisorTriplet(self, nums: List[int]) -> int:
    def is_single_divisor_triplet(i, j, k):
        s = i + j + k
        if s % i == 0: return s % j != 0 and s % k != 0
        if s % j == 0: return s % k != 0
        return s % k == 0
    
    tuples = [(i, j, k) for i in range(1, 101) for j in range(i, 101) for k in range(j, 101) if is_single_divisor_triplet(i, j, k)]
    
    occ = Counter(nums)
    
    def count_of_triplets(i, j, k):
        if i == j or j == k:
            return occ[j] * (occ[j] - 1) // 2 * occ[i if j == k else k]
        return occ[i] * occ[j] * occ[k]
        
    return 6 * sum([count_of_triplets(*tup) for tup in tuples])

      
      
      
