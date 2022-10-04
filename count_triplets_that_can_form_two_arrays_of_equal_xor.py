'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
'''


    def countTriplets(self, A):
        A.insert(0, 0)
        n = len(A)
        for i in xrange(n - 1):
            A[i + 1] ^= A[i]
        res = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if A[i] == A[j]:
                    res += j - i - 1
        return res
      
-----------------------------------------------------------------------------

# IDEA: if a == b it means a ^ b == 0, so we need to find all subarrays that XOR to 0; every such subarray with N elements
#       can be split into N-1 triplets (since we can't have empty 'a' or 'b'); use nested loop to find all subarrays
#       O(N^2) time, O(1) space
#
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)-1):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    res += j-i # len-1
        return res
