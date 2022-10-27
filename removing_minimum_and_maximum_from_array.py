'''
You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
'''

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        ind_max = nums.index(max(nums))
        ind_min = nums.index(min(nums))

        print(ind_max)
        print(ind_min)

        # delete from the front:

        front = max(ind_max, ind_min) + 1 \

        print('front %d' % front)

        back = len(nums) - min(ind_max, ind_min)
        print('back %d ' % back)

        both = min(ind_min, ind_max) + len(nums) - max(ind_min, ind_max)+1
        print('both %d' % both)
        return min(front,back,both)
      
-----------------------------------------------------------------------------------------------
    def minimumDeletions(self, A):
        i, j, n = A.index(min(A)), A.index(max(A)), len(A)
        return min(max(i + 1, j + 1), max(n - i, n - j), i + 1 + n - j, j + 1 + n - i)
      
------------------------------------------------------------------------------------------------------------     

Explanation:

There are only 4 cases to consider.

Case 1: [1,10000,5,6,7,8,9,2] - It's optimal to grab both from the front.

Case 2: [2,3,4,5,6,7,10000,1] - It's optimal to grab both from the back.

Case 3: [2,3,10000,5,6,7,4,1] - It's optimal to grab the max from the front and min from back.

Case 4: [2,3,1,5,6,7,4,10000] - It's optimal to grab the min from the front and max from back.

Consider them all and take the minimum.

Code:

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minFromFront = nums.index(min(nums))
        maxFromFront = nums.index(max(nums))
        
        minFromBack = len(nums) - minFromFront - 1
        maxFromBack = len(nums) - maxFromFront - 1 
        
        return min(max(minFromFront, maxFromFront) + 1,  # Case 1
                   max(minFromBack, maxFromBack) + 1,    # Case 2
                   minFromBack + maxFromFront + 2,       # Case 3 
                   minFromFront + maxFromBack + 2)       # Case 4
