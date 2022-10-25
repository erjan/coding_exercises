'''
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.
'''


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pows = [2 ** i for i in range(0,22)] # form our list of powers of 2
        dp_seen = {} # dict to store what we've seen - dynamic programming solution for time requirement
        count = 0 # to store the answer

        for j in range(0, len(deliciousness)):
            for i in range(0, len(pows)):
                if pows[i] - deliciousness[j] in dp_seen: # "if we find a previous deliciousness[j] as pows[i] - deliciousness[j], then we will add dp_seen[deliciousness[j]] to count"
                    count += dp_seen[pows[i] - deliciousness[j]]
            if deliciousness[j] in dp_seen:
                dp_seen[deliciousness[j]] += 1 
            else:
                dp_seen[deliciousness[j]] = 1
                
        return count % (10**9 + 7) # the arbitrary modulo, presumably to reduce the answer size
