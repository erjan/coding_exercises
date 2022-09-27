'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
		#Function to compute factorial
        def factorial(z):
            y = 1
            for i in range(1,z+1):
                y *= i
            return y
			
        #list of numbers 1 to n that we pull from
        nums = [str(i) for i in range(1, n+1)]
		
		#set k to k-1 for 0 indexing
        k -= 1
		
		#initialize our result
        res = ''
        
		#repeat the process until there are no more digits remaining to use
        while nums:
		
			#calculate factorial of remaining len(nums) - 1
            f = factorial(len(nums)-1)
			
			#find index in nums to use as next digit
            idx = k//f
			
			#remove this digit from nums and add it to the result
            res += nums.pop(idx)
			
			#update k for the next loop through
            k = k % f
            
        return res
