'''
You are given a 0-indexed positive integer array nums and a positive integer k.

A pair of numbers (num1, num2) is called excellent if the following conditions are satisfied:

Both the numbers num1 and num2 exist in the array nums.
The sum of the number of set bits in num1 OR num2 and num1 AND num2 is greater than or equal to k, where OR is the bitwise OR operation and AND is the bitwise AND operation.
Return the number of distinct excellent pairs.

Two pairs (a, b) and (c, d) are considered distinct if either a != c or b != d. For example, (1, 2) and (2, 1) are distinct.

Note that a pair (num1, num2) such that num1 == num2 can also be excellent if you have at least one occurrence of num1 in the array.
'''


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        
        # Brute Force
        # s=set()
        # for i in range(n):
        #     for j in range(n):
        #         a=nums[i] | nums[j]
        #         b=nums[i] & nums[j]
        #         a_count=bin(a).count('1')
        #         b_count=bin(b).count('1')
        #         if a_count+b_count>=k and (nums[i], nums[j]) not in s:
        #             s.add((nums[i], nums[j]))
        #             count+=1
        # return count
        
        arr=[]
        for num in set(nums):
            arr.append(bin(num).count('1'))
        arr.sort()
        l=0
        r=len(arr)-1
        ans=0
        while l<=r:
            if arr[l]+arr[r]>=k:
                ans+=(r-l)*2 + 1
                r-=1
            else:
                l+=1
        return ans
      
---------------------------------------------------------------------------------------------------------
class Solution:
	def countExcellentPairs(self, nums: List[int], k: int) -> int:
		# Count the Number of Bits in Each Unique Number - O(n)
		# Tally the Number of Times Each Bit Count Occurs - O(n)
		# Sort the (bit count, tally) pairs by bit count - O(nlogn)
		counts = sorted(Counter(map(int.bit_count, set(nums))).items()) # (I am fully aware that this line of code is really doing too much work)

		# Compute the Reversed Prefix Sum of the Tallies (i.e. sums[i] is how many numbers have at least counts[i][0] '1' bits) - O(n)
		sums = [0]*len(counts)
		sums[-1] = counts[-1][1]
		for i in range(len(sums) - 2, -1, -1):
			sums[i] += counts[i][1] + sums[i + 1]

		# Choose Each Number as the First Number of a Pair - O(nlogn)
		pairs = 0
		for n, c in counts:
			# Find the Smallest Number Which Forms a Valid Pair - O(logn)
			i = bisect_left(counts, k - n, key = lambda x: x[0])

			# Check if Any Pairs Can be Formed
			if i < len(sums):
				# Compute the Number of Pairs Which Start With the Given Collection of Numbers
				pairs += c*sums[i]

		# Return the Number of Pairs
		return pairs
