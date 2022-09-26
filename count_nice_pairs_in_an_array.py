'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.


The above equation can be modified as -

num[i] - rev(num[i]) = num[j] - rev(num[j])
We can see that we are required to find 
number of pairs whose difference between original number and reversed number is the same. So, we can just count the frequency of numbers having a particular n - rev(n) value and store them in a hashmap. Finally, we just have to count the pairs which can be formed which is freq[i] * (freq[i] - 1) / 2.
'''

def countNicePairs(self, nums: List[int]) -> int:
	freqs = Counter(num - int(str(num)[::-1]) for num in nums)
	return sum(freq * (freq - 1) // 2 for freq in freqs.values()) % 1000000007
