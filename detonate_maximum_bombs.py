'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
'''

class Solution(object):
    def maximumDetonation(self, bombs):
        def count(i):
            dq, ret = [i], [i]
            while len(dq) > 0:
                i = dq.pop()
                for j in adj[i]:
                    if j not in ret and j not in dq:
                        dq.append(j)
                        ret.append(j)
            return len(ret)

        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                    adj[i].append(j)
                if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[j][2] ** 2:
                    adj[j].append(i)
        ret = 0
        for i in range(len(bombs)):
            ret = max(ret, count(i))
        return ret
