'''
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.
'''

def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                count += n-1-i
        return count
      
--------------------------------------------------------------
'''
Intuition

Go through numbers and their counts in decreasing order of numbers
We keep track of remaining numbers we need to change in each iteration and add it to result
Explanation

sorted(Counter(nums).items(), reverse=True) gives items and their counts in reverse order
We are doing items() instead of just taking values() as we want to order the elements in dictionary by the keys and not values.
Example

let's take a look at [1,2,2,5,5,43]
we look at 43 and add 1 to to_change (as one of 43 needs to be changed to next number)
we look at 5 and add to_change to result (changing 43 to 5), and add 2 of 5, which is new_elements to to_change. Now we have 3 to_change
We do so until the end when we are at 1, and we end up adding remaining 2s to the result.
Complexity

O(NlogN) time for sorting operation.
O(N) space for storing the counts.
'''

def reductionOperations(self, nums: List[int]) -> int:
	res = to_change = 0
	for _, new_elements in sorted(Counter(nums).items(), reverse=True):
		res += to_change
		to_change += new_elements
	return res
