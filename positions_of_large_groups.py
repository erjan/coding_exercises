'''
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
'''


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
            i = 0
            res = list()
            q = [[c, len(list(group))] for c, group in itertools.groupby(s)]

            for k, v in q:

                if v >= 3:
                    res.append([i, i + v - 1])
                i += v
            print(res)
            return res
