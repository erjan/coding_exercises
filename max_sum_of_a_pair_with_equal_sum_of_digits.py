'''
You are given a 0-indexed array nums consisting of positive integers. You can 
choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
'''

from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        c=defaultdict(list)
        nums.sort()
        ## Approach:
        ## Find some of digits of all numbers
        ## Store the sum value in a dictionary. The sum value is the key and the number itself is appended in a list
        ## This gives me all the numbers that has some particular value as sum
        ## Numbers are sorted in ascending order, so the list corresponding to the digits sums also gets sorted automatically
        for x in nums:
            y=x
            t=0
            while x:
                t+=x%10
                x//=10
            c[t].append(y)

        res=-1
        for x in c:
            if len(c[x])>1:
                y=c[x]
                res=max(res,y[-1]+y[-2])
        return res
      
------------------------------------------------------------      

class Solution:     # The plan here is to:
                    # 
                    #   • sort the elements of nums into a dict of maxheaps,
                    #     according to sum-of-digits.
                    #
                    #   • For each key, determine whether there are at least two 
                    #     elements in that key's values, and if so, compute the
                    #     product of the greatest two elements.
                    #
                    #   • return the the greatest such product as the answer.

                    # For example:
					
                    #     nums = [6,15,13,12,24,21] –> {3:[12,21], 4:[13], 6:[6,15,24]}
					
                    #     Only two keys qualify, 3 and 6, for which the greatest two elements
                    #     are 12,21 and 15,24, respectively. 12+21 = 33 and 15+24 = 39,
                    #     so the answer is 39.

    def maximumSum(self, nums: List[int]) -> int:
        d, mx = defaultdict(list), -1
        digits = lambda x: sum(map(int, list(str(x))))      # <-- sum-of-digits function
       
        for n in nums:                                      # <-- construct max-heaps
            heappush(d[digits(n)],-n)                       #     (note "-n") 

        for i in d:                                         # <-- pop the two greatest values off
            if len(d[i]) > 1:                               #     each maxheap (when possible) and
                mx= max(mx, -heappop(d[i])-heappop(d[i]))   #     compare with current max value.
                                                           
        return mx
      
