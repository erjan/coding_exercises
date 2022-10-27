'''
You are given a 2D integer array groups of length n. You are also given an integer array nums.

You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).

Return true if you can do this task, and false otherwise.

Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.
'''

#without KMP
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # transform groups list into str
        for i in range(len(groups)):
            l1=[str(m) for m in groups[i]]        
            s='_'.join(l1)
			#To prevent errors like the one below, we need to decorate each string
			#in case some problem like groups=[[12,1]]   nums=[2,1]
            s='_'+s+'_'
            groups[i]=(s,len(s))
            
        # also we transform the nums into str
        l=[str(m) for m in nums]
        str_nums='_'.join(l)
		#This step is to facilitate starting position matching
        str_nums='_'+str_nums+'_'
        
        for item in groups:
            if item[0] not in str_nums :
                return False
			#if it matches we cut the front part
            idx=str_nums.index(item[0])
            str_nums=str_nums[idx+item[1]-1:]
        return True
      
---------------------------------------------------------------------------------------------------------------------------------      
#KMP

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        sz, idx = len(nums), 0
        for group in groups:
            groupSize, LPS = len(group), [0] * len(group)
            for i in range(1, groupSize):
                j = LPS[i - 1]
                while j > 0 and group[i] != group[j]:
                    j = LPS[j - 1]
                if group[i] == group[j]:
                    j += 1
                LPS[i] = j
            j = 0
            while idx < sz:
                if nums[idx] == group[j]:
                    j += 1; idx += 1
                if j == groupSize:
                    break
                else:
                    if idx < sz and nums[idx] != group[j]:
                        if j > 0:
                            j = LPS[j - 1]
                        else:
                            idx += 1
            if j != groupSize:
                return False
        return True
      
---------------------------------------------------------
#intuitive solution

class Solution(object):
    def canChoose(self, groups, nums):
        res = 0
        i = 0
        for arr in (groups):
            m = len(arr)
            while i+m < (len(nums))+1:
                if nums[i:m+i] == arr:
                    i += m
                    res += 1
                    break
                i +=1
                
        return res == len(groups)

