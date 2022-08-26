'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''

from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        last_seen = dict()

        for i, k in enumerate(s):
            last_seen[k] = i

        res = []

        start = 0
        end = 0

        for i, c in enumerate(s):
            print('------------------------------')
            print(f'{i,c}')
            end = max(end, last_seen[c])
            print('end is ' + str(end))
            if i == end:
                print('found partition')
                res.append(end-start+1)
                start = i+1
        return res
