'''
You are given a 0-indexed integer array nums. In one operation, you can:

Choose two different indices i and j such that 0 <= i, j < nums.length.
Choose a non-negative integer k such that the kth bit (0-indexed) in the binary representation of nums[i] and nums[j] is 1.
Subtract 2k from nums[i] and nums[j].
A subarray is beautiful if it is possible to make all of its elements equal to 0 after applying the above operation any number of times.

Return the number of beautiful subarrays in the array nums.

A subarray is a contiguous non-empty sequence of elements within an array.
'''




'''
Bits in a beautiful subarray should appear even number of times.

Therefore, XOR of elements of a beautiful subarray should be zero.

Counting subarrays with a specific XOR in O(n) is a classic problem (you can find it by the name).
'''

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = Counter({0: 1})
        for val in accumulate(nums, operator.xor):
            cnt[val] += 1
        return sum(v * (v - 1) // 2 for v in cnt.values())
      
----------------------------------------------------------------------------------------------
Approach
Define the function beautifulSubarrays that takes a list of integers nums as input and returns an integer.
Initialize a variable res to 0 to keep track of the number of beautiful subarrays.
Get the length of the input list nums and store it in a variable n.
Initialize a list pre_xor with n+1 elements and fill it with zeros.
Set the first element of pre_xor to 0.
Initialize a list cnt with (1<<20) elements and fill it with zeros. This list will be used to count the number of occurrences of each prefix xor value.
Set the first element of cnt to 1, since the empty subarray has a prefix xor of 0.
Loop through the indices i in the range [1, n]:
Compute the prefix xor value of the subarray nums[0:i] and store it in pre_xor[i].
Update the res variable by adding the value of cnt[pre_xor[i]].
Increment the value of cnt[pre_xor[i]].
Return the value of res.
Complexity
Time complexity:
Space complexity:
Code
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        pre_xor = [0] * (n+1)
        pre_xor[0]=0
        cnt = [0]*(1<<20)
        cnt[0] = 1
        
        for i in range(1,n+1):
            pre_xor[i] = pre_xor[i-1] ^ nums[i-1]
            res += cnt[pre_xor[i]]
            cnt[pre_xor[i]] += 1

        return res
