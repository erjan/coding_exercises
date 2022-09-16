'''
You are given a 0-indexed integer array nums. In one operation, select any non-negative integer x and an index i, then update nums[i] to be equal to nums[i] AND (nums[i] XOR x).

Note that AND is the bitwise AND operation and XOR is the bitwise XOR operation.

Return the maximum possible bitwise XOR of all elements of nums after applying the operation any number of times.
'''

Explanation
The maximum possible result is res = A[0] || A[1] || A[2] ... and it's realisiable.

Prove
Now we approve it's realisiable.
Assume result is best = XOR(A[i]) and best < res above.
There is at least one bit difference between best and res, assume it's x = 1 << k.

We can find at least a A[i] that A[i] & x = x.

we apply x on A[i], A[i] is updated to A[i] & (A[i] ^ x) = A[i] ^ x.
We had best = XOR(A[i]) as said above,
now we have best2 = XOR(A[i]) ^ x,
so we get a better best2 > best, where we prove by contradiction.


Complexity
Time O(n)
Space O(1)

   def maximumXOR(self, nums):
        return reduce(ior, nums)
    
    
------------------------------------------------------------------------------------------------
class Solution(object):
	def maximumXOR(self, nums):
		#approach1
#         lis=[0 for _ in range(32)]
#         for i in range(32):
#             for j in nums:
#                 if 1<<i & j:
#                     lis[i]=1
#                     break
#         s=0
#         val=1

#         for i in range(32):
#             if lis[i]:
#                 s+=val
#             val*=2
#         return s

#approach2
#as we know we have to find the xor of all the elements
#so we can observe there that we are calculating the sum only(of the odd bits)
#lets take example
#[3,2,4,6]
#3-0011
#2-0010
#4-0100
#6-0110
#so we have to find only odd bit sum
#so we make the 6th 3rd bit 0 to make the odd bit at the 3rd position
#and we know that if there exist 1 in any number at that position then we can make others 0 and take the first one to make the odd
#so here we are taking the or (which will take only the set bits - as we know 0 or 0 means 0 and 1 for all other cases)
		r = 0
		for num in nums:
			r |= num
		return r

		"""
		:type nums: List[int]
		:rtype: int
		"""
