'''
You are given a 0-indexed integer array nums.

The effective value of three indices i, j, and k is defined as ((nums[i] | nums[j]) & nums[k]).

The xor-beauty of the array is the XORing of the effective values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.

Return the xor-beauty of nums.

Note that:

val1 | val2 is bitwise OR of val1 and val2.
val1 & val2 is bitwise AND of val1 and val2.
'''


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
      
'''      
Many of you may get accepted during contest by guessing the answer (the bitwise XOR of all num in nums). Here we provide a formal proof.

Key Observations:
Fully utilize the symmetry between i, j, k.
a ^ a = 0 (the property of bitwise XOR).
Proof:
First, note that by symmetry of i and j, we know that the value of ((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) are equal. Which then implies that for a pair of (i, j) where i != j, the bitwise XOR of ((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) is 0. Thus, we only need to deal with the triplets (i, j, k) where i == j.

Now we only need to consider the triplets (i, j, k) where i == j, so that ((nums[i] | nums[j]) & nums[k]) = ((nums[i] | nums[i]) & nums[k]) = nums[i] & nums[k]. By symmetry of i and k, we know that the value of nums[i] & nums[k] and nums[k] & nums[i] are equal. Which then implies that for a pair of (i, k) where i != k, the bitwise XOR of nums[i] & nums[k] and nums[k] & nums[i] is 0. Thus, we only need to deal with the case of i == k.

Therefore, we only need to consider the triplets (i, j, k) where i == j == k, and the final answer reduces to the bitwise XOR of ((nums[i] | nums[j]) & nums[k]) = ((nums[i] | nums[i]) & nums[i]) = nums[i].

Complexity
Time complexity: O(N)
Space complexity: O(1)
Code

'''

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)        
