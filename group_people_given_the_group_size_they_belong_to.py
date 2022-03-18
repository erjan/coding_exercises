'''
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
'''

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        
        d = dict()
        
        for i,group in enumerate(groupSizes):            
            if group not in d:
                d[group] = [i]                
            else:
                d[group].append(i)   
                
            if len(d[group]) == group:
                res.append(d[group])
                del d[group]
        return res
