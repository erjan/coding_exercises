'''
You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

Return the number of pairs of interchangeable rectangles in rectangles.
'''

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = defaultdict(int)
        for x, y in rectangles:
            ratios[x/y] += 1
        res = 0
        for val in ratios.values():
            res += (val*(val-1)//2)
        return res
      
-----------------------------------------------------------------------
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dic={}
        for i,j in rectangles:
            if i/j not in dic:
                dic[i/j]=1
            else:
                dic[i/j]+=1
        return sum(val*(val-1)//2 for val in dic.values())
      
------------------------------------------------------------------------------------
Give every rectangle ratio in rectangles and clarify i > j or j > i.
Count every ratio pairs.
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = [r[0] / r[1] if r[1] > r[0] else - r[1] / r[0] for r in rectangles]
        length, result = len(ratio), 0
        times = Counter(ratio).most_common(length)
        for times in times:
            result += times[1] * (times[1] - 1) // 2
        return result
