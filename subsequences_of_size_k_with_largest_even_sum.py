'''
You are given an integer array nums and an integer k. Find the largest even sum of any subsequence of nums that has a length of k.

Return this sum, or -1 if such a sum does not exist.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,1,5,3,1], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,5,3]. It has a sum of 4 + 5 + 3 = 12.
Example 2:

Input: nums = [4,6,2], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.
Example 3:

Input: nums = [1,3,5], k = 1
Output: -1
Explanation:
No subsequence of nums with length 1 has an even sum.
'''


First, get the sum of top k largest numbers res.
If res is even, just return it.
Otherwise, res is odd and we just need to change one number, that is, replace an odd number by an even number or vise versa. More specifically:
replace the smallest even number from res by the largest odd number from the rest of the array, or
replace the smallest odd number from res by the largest even number from the rest of the array.
image

Therefore:

image

Just iterate over the rest of the array and check if either of the replacement above is possible and save the largeset result.
If no replacement happens after the iteration, return -1, otherwise, return the largest result.
def largestEvenSum(self, A: List[int], k: int) -> int:
        A.sort(reverse = True)
        n = len(A)
        res = sum(A[:k])
        
        if res % 2 == 0: return res
        
        odd, even = 10 ** 6, 10 ** 6
        
        for i in range(k):
            if A[i] % 2: odd = min(odd, A[i])
            else: even = min(even, A[i])
                
        ans = -1
        for i in range(k, n):
            if A[i] % 2 and even != 10 ** 6:
                ans = max(ans, res - even + A[i])
            if A[i] % 2 == 0 and odd != 10 ** 6:
                ans = max(ans, res - odd + A[i])
        
        return ans
      
-------------------------------------------------------
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            even = [num for num in nums if num % 2 == 0]
            return max(even) if len(even) != 0 else -1
        if k == n:
            return sum(nums) if sum(nums) % 2 == 0 else -1
        if k > n:
            return -1
        
        prefix_even = [0]
        prefix_odd = [0]
        
        for num in reversed(sorted(nums)):
            if num % 2 == 1:
                prefix_odd.append(prefix_odd[-1] + num)
            else:
                prefix_even.append(prefix_even[-1] + num)
                
        res = -math.inf
        for i in range(k+1):
            j = k - i
            if i < len(prefix_even) and j < len(prefix_odd) and (prefix_even[i] +  prefix_odd[j]) % 2 == 0:
                res = max(res,  prefix_even[i] +  prefix_odd[j])
        return res if res != -math.inf else -1
      
----------------------------------------------------------------------
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # even = odd * even + even
        nums = sorted(nums)[::-1] 
        if sum(nums[:k]) %2 ==0 :
            return sum(nums[:k])
        
        remove_odd = None
        remove_even = None
        for n in  nums[:k]:
            if n%2==1:
                remove_odd = n
            else:
                remove_even = n
        add_even = None
        add_odd = None
        for n in reversed(nums[k:]):
            if n%2 == 0:
                add_even = n
            else:
                add_odd = n
            
             
        if  (  add_odd is None or   remove_even is None) and  (  remove_odd is None or   add_even is None):
            return -1
        
         
        if  add_even is None or  remove_odd is None:
            return sum(nums[:k]) +  add_odd-remove_even
        if   add_odd is None or   remove_even is None:
            return sum(nums[:k]) + add_even-remove_odd
        return sum(nums[:k]) + max( add_even-remove_odd, add_odd-remove_even)
--------------------------------------------------------------------------------------
# Approach 1: 
# Time: O(nlogn)
# Space:O(n)

# Algorithm:
# First, get the sum of top k largest numbers res.
# If res is even, just return it.
# Otherwise, res is odd and we just need to change one number, that is, replace an odd number by an even number or vise versa. More specifically:
# replace the smallest even number from res by the largest odd number from the rest of the array, or
# replace the smallest odd number from res by the largest even number from the rest of the array.

def largestEvenSum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort(reverse = True)
    n = len(nums)
    topkSum = sum(nums[:k])

    if topkSum % 2 == 0: 
        return topkSum

    minOdd = minEven = float('inf')

    for i in range(k):
        if nums[i] % 2 == 1:
            minOdd = min(minOdd, nums[i])
        else:
            minEven = min(minEven, nums[i])

    ret = -1
    for i in range(k,n):
        if nums[i] % 2 == 1 and minEven != float('inf'):
            ret = max(ret, topkSum + nums[i] - minEven)
        if nums[i] % 2 == 0 and minOdd != float('inf'):
            ret = max(ret, topkSum + nums[i] - minOdd)

    return ret
-------------------------------------------------------------
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        o, e = -1, -1
        best = 0
        
        for i in range(k):
            best += nums[i]
            if nums[i] % 2:
                o = i
            else:
                e = i
        
        if best % 2 == 0:
            return best
        
        no, ne = -1, -1
        for i in range(len(nums) - 1, k - 1, -1):
            if nums[i] % 2:
                no = i
            else:
                ne = i

        res = -1
        if o != -1 and ne != -1:
            res = max(res, best + nums[ne] - nums[o])
        if e != -1 and no != -1:
            res = max(res, best + nums[no] - nums[e])
        return res
  
      
      
