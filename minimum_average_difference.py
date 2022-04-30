'''
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of 
the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
'''


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre = list()
        res=float('inf')
        pre.append(nums[0])
        for i in range(1,n):
            pre.append(nums[i] + pre[i-1])
        
        p=0
        post=[0]*n
        for i in range(n-1,-1,-1):
            post[i]=p
            p+=nums[i]
        
        for i in range(n):
            
            if pre[i]>0:
                first = int(pre[i]/(i+1))            
            else:
                first = 0
            
            if post[i] > 0 and n - i -1 >0:
                second = int(post[i]/(n-i-1))
            else:
                second = 0
            
            if abs(first - second) < res:
                res = abs(first-second)
                idx = i
        return idx
                
            
                
            
        
        
        
        
#         n=len(nums)
        
#         p=0
#         pre=[]
#         for i in range(n):
#             p+=nums[i]
#             pre.append(p)
        
#         p=0
#         post=[0]*n
#         for i in range(n-1,-1,-1):
#             post[i]=p
#             p+=nums[i]

#         res=float('inf')
#         idx=0
#         for i in range(n):
#             first = int(pre[i]/(i+1)) if pre[i]>0 else 0
#             second = int(post[i]/(n-i-1)) if post[i]>0 and n-i-1>0 else 0
#             if abs(first-second)<res:
#                 idx=i
#                 res=abs(first-second)
#         return idx
