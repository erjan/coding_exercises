'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
nums[i] - nums[j] == k
Notice that |val| denotes the absolute value of val.
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        c=Counter(nums)
        
        if k==0:
            for key,v in c.items():
                if v>1:
                    cnt+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    cnt+=1
        return cnt
-------------------------------------------------------------------------

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
		#If k is less than 0, then the result is 0 since we are looking fpr pairs with an ABSOLUTE difference of k.
        if k < 0:
            return 0
        
        count = Counter(nums)
        pairs = set([])
        
        for num in count.keys():
			#Special case: If k == 0, then there needs to be at least two occurences of a particular num in nums 
			#in order for there to be a pair (num, num).
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))
					
			#Regular case: k != 0. Simply check if num + k is a member of the array nums.
			#Insert the pair into the set of pairs (smallerNum, largerNum) so that there are no duplicate pairs.
            else:
                otherNum = num + k
                if otherNum in count:
                    pairs.add((num, otherNum) if num <= otherNum else (otherNum, num))
                    
        return len(pairs)
