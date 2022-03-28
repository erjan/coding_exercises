'''
Find the number with the most occurrences in the given array.
When the number of occurrences is the same, return the smallest one.
'''

from collections import Counter

class Solution:
  
    def find_number(self, array: List[int]) -> int:
        # Write your code here.

        d = dict(Counter(array))

        maxval = -1
        maxkey = -1

        for k,v in d.items():

            if v > maxval:
                maxval = v
                maxkey = k
            elif v == maxval and k < maxkey:
                maxval = v
                maxkey = k
        return maxkey

    
#my solution

        n = array
        d = dict(Counter(n))
        d = list(d.items())

        d = sorted(d, key = lambda x: x[0], reverse=True)

        d = sorted(d, key = lambda x: x[1], reverse=True)
        most_freq = d[0][1]

        res = 0
        for i in range(len(d)-1,-1,-1):
            if most_freq == d[i][1]:
                return d[i][0]
