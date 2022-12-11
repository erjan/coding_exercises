'''
There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] represents the ith square with a side length of sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the height of the current tallest stack of squares.

Return an integer array ans where ans[i] represents the height described above after dropping the ith square.
'''

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        for i, (x, l) in enumerate(positions): 
            val = 0
            for ii in range(i): 
                xx, ll = positions[ii]
                if xx < x+l and x < xx+ll: val = max(val, ans[ii])
            ans.append(val + l)
        for i in range(1, len(ans)): ans[i] = max(ans[i-1], ans[i])
        return ans
      
------------------------------------------------------------------------------------
class Solution:
    def fallingSquares(self, positions):
            height, pos, max_h,res = [0],[0],0,[]
            for left, side in positions:
                i = bisect.bisect_right(pos, left)
                j = bisect.bisect_left(pos, left + side)
                high = max(height[i - 1:j] or [0]) + side 
                pos[i:j] = [left, left + side]
                height[i:j] = [high, height[j - 1]]
                max_h = max(max_h, high)
                res.append(max_h)
            return res
          
---------------------------------------------------------------------------------------------------          
