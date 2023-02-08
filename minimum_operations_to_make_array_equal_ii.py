'''
You are given two integer arrays nums1 and nums2 of equal length n and an integer k. You can perform the following operation on nums1:

Choose two indexes i and j and increment nums1[i] by k and decrement nums1[j] by k. In other words, nums1[i] = nums1[i] + k and nums1[j] = nums1[j] - k.
nums1 is said to be equal to nums2 if for all indices i such that 0 <= i < n, nums1[i] == nums2[i].

Return the minimum number of operations required to make nums1 equal to nums2. If it is impossible to make them equal, return -1.

Some considerations:

If k==0, the answer is either-1or0, depending whether nums1 != nums2.
For each i,nums1[i]-num2[i] == quo * kwherequo is the number of moves on nums1[i], num2[i], so it follows that(nums1[i]-num2[i])%k == 0for each iif the arrays can be made equal.
A solution exists if and only if the sum of all quo is zero, because each move does not change the value of sum(nums1)+sum(nums2).
The value of sum(abs(quo))for of all quoincreases by two for each move, which is equivalent to saying that the number of moves should be sum(abs(ni))//2.
'''


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if not k: return -(nums1 != nums2)

        sm = smAbs = 0

        for i in range(len(nums1)):

            diff = nums1[i]-nums2[i] 

            if diff%k: return -1
            quo = diff//k

            sm   += quo
            smAbs+= abs(quo)

        return -1 if sm else smAbs//2
