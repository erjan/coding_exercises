'''
You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.
'''


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        F = [0]*len(nums)
        n = len(nums)
        F[0] =sum([i*nums[i] for i in range(n)]) #can be initialized using the function
        sum_nums = sum(nums)
        for i in range(n-1):
            F[i+1] = F[i] - n * nums[-1-i] +sum_nums
        return max(F)
      
---------------------------------------------------------------------------------------------------      

Now observe how the array total changed:

(1 rotation) - (no rotation) = 4·a - 1·b - 1·c - 1·d - 1·e
                             = 5·a - 1·a - 1·b - 1·c - 1·d - 1·e
							 = 5·a - (1·a + 1·b + 1·c + 1·d + 1·e)
							 = N·a - sum(A)
							 = N·A[i] - sum(A)
		  ∴ (i + 1 rotation) = N·A[i] - sum(A) + (i rotation)
Where N is the length of array A. Now, we can calculate the total once (#1). And find the total for the next rotation in O(1) time using the equation above (#2).

def maxRotateFunction(self, A: List[int]) -> int:

	sum_A = sum(A)
	N = len(A)
	res = sum(i*a for i,a in enumerate(A)) # 1
	total = res                            # 1

	for i in range(len(A)):
		total += N*A[i] - sum_A # 2
		res = max(res, total)

	return res
  
