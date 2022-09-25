'''
Given an array of integers arr, find the sum of min(b), where 
b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
'''

'''
It's easy to see why this happens: our subarrays ending with i-th value are basically same subarrays for (i-1)-th value with extra element A[i] added to each one of them and plus one extra subarray consisting of singular value A[i]. Adding same or bigger value to subarrays 
doesn't change their minimal values. Thus we can reuse previous sum and account for that extra singular subarray, thus result[i] = result[i-1] + A[i]
'''

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)
