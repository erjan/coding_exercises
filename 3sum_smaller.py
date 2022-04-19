'''
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
 
 '''

def threeSumSmaller(self, nums, target):
    count = 0
    nums.sort()
    for i in xrange(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                count += k-j
                j += 1
            else:
                k -= 1
    return count
  
------------------------------------------------------

After sorting, if i, j, k is a valid triple, then i, j-1, k, ..., i, i+1, k are also valid triples. No need to count them one by one.

def threeSumSmaller(self, nums, target):
    nums.sort()
    count = 0
    for k in range(len(nums)):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] + nums[k] < target:
                count += j - i
                i += 1
            else:
                j -= 1
    return count
--------------------------------------------

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        # If we have no triplets we cant find a valid answer so return 0
        if len(nums) < 3:
            return 0
        
        # Result that will be returned
        res = 0 
        
        # We need to sort out array because the question is asking for
        # triplets that are "sorted" i < j < k <, so you cant have an unsorted triplet
        # like 1,3,2
        nums.sort() 
         
        # We need to iterate through the array up until the last 2 numbers
        # We don't need to check the last two numbers because their wont be enough
        # numbers left to complete a triplet
        #
        # EX: [-2,0,0,1,3]
        for i in range(len(nums) - 2):
            
            # Here we keep track of our two pointers, we need to start at i+1 because we are
            # splitting this into a two sum problem
            #
            # [-2] => [0,0,1,3]
            #          L     R
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # Calculate the total sum to of the current index, right pointer and left pointer
                three_sum = nums[i] + nums[left] + nums[right]
                
                # If we have a valid triplet we need to increment our result
                #
                # Q. Why do we increment by doing right - left? 
                # A. The array is sorted, we know every combination will fit if we kept moving the right
                #    pointer left, why do the extra work? Look at the example below:
                #
                # [-2] => [0,0,1,3]
                #          L     R
                #
                # [-2] => [0,0,1,3]
                #          L   R
                #
                # [-2] => [0,0,1,3]
                #          L R
                if three_sum < target:
                    res += right - left
                    
                    # Move the left pointer to see if we can find any more valid answers (left increases the sum)
                    left += 1
                else:
                    # Move the right pointer to see if we can find any more valid answers (right decreases the sum)
                    right -= 1

        return res
--------------------------------------------------------------------

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        #sort array to achieve 0 <= i < j < k < n property
        nums.sort()
        result = 0
        #iterate through array till len -2 
        for i in range(len(nums)-2):
            # start find another two numbers by starting new j,k pointers 
            #j = next to current
            #k = end of listt
            j = i+1
            k = len(nums)-1
            
            #while j and k is not cross each other
            while j < k:
                #get total of three numbers
                tot = nums[i]+nums[j]+nums[k]
                #if sum of three numbers less than target
                if tot < target:
                    # since array is sorted,
                    # we can create triplets that less than target,from all numbers from j to k 
                    result += k-j
                    #increase left pointer by one to find another set of triplets
                    j+=1
                #if total is greater than target,we need a smaller total,so to decrease total move right pointer 
                else:
                    k-=1
        return result
--------------------------------------------------------------------------------------------------

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        counter=0
        nums.sort()
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo<hi:
                k=nums[i]+nums[lo]+nums[hi]
                #print(nums[i],nums[lo],nums[hi])
                if target-k>0:
                    counter+=hi-lo
                    lo+=1
                else:
                    hi-=1                       
        return counter
      
      
      
      
  
