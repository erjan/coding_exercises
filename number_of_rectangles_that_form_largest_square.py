'''
You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. 
For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
'''

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sq = list()
        r = rectangles
        for i in range(len(r)):
            rect = r[i]
            l = rect[0]
            w = rect[1]
            side = min(l, w)
            sq.append(side)

        m = max(sq)

        res = sq.count(m)
        print(res)
        return res
