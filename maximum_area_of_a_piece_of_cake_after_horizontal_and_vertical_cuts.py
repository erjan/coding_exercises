'''
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake 
after you cut at each horizontal and vertical position 
provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7
'''

def maxArea(self, h: int, w: int, H: List[int], V: List[int]) -> int:
	def getMaxGap(nums, max_size):
		maxGap = max(nums[0], max_size - nums[-1])
		for i in range(1, len(nums)):
			maxGap = max(maxGap, nums[i] - nums[i - 1])
		return maxGap
	return getMaxGap(sorted(H), h) * getMaxGap(sorted(V), w) % 1000000007

-------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        maxh, maxv = max(hc[0], h - hc[-1]), max(vc[0], w - vc[-1])
        for i in range(len(hc)):
            maxh = max(maxh, hc[i] - hc[i-1])
        for i in range(len(vc)):
            maxv = max(maxv, vc[i] - vc[i-1])
        return (maxh * maxv) % 1000000007
      
---------------------------------------------------------------------------------------------------------------    

class Solution:
    def maxArea(self, h: int, w: int, h2: List[int], v: List[int]) -> int:
        
        
        h2.sort()
        v.sort()

        maxh = max(h2[0], h - h2[-1])
        maxv = max(v[0], w- v[-1])

       

        for i in range(len(h2)-1):
            maxh = max(maxh, abs(h2[i] - h2[i+1]))

       
        for i in range(len(v)-1):

            maxv = max(maxv, abs(v[i] - v[i+1]))

        res = maxh*maxv
        return res % (10**9+7)
