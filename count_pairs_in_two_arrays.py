'''
Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j) such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.

 

Example 1:

Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
Output: 1
Explanation: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.
Example 2:

Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
Output: 5
Explanation: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.
'''


Explanation
nums1[i] + nums1[j] > nums2[i] + nums2[j], i < j can be converted to
(nums1[i]-nums2[i]) + (nums1[j]-nums2[j]) > 0, i < j
At this point, you will realize that the constrain i < j is not really important anymore, you can replace i with j and get
(nums1[j]-nums2[j]) + (nums1[i]-nums2[i]) > 0. This is due to Commutative_Property of Addition.
We can calculate the difference between nums1[i] and nums2[i] and sort the result array diff
Then for each diff[i], we want to find number of diff[j] such that diff[j] > -diff[i], so that diff[i] + diff[j] > 0
Remember the original order is not important as discussed above, we will only focus on current order (i.e. only count j such that j > i)
This part can be confusing, the original order also requires to find j such that j > i, but this is totally different from the order of diff. This is because that diff is already sorted, which breaks the original order.
Since diff is already sorted, we can use binary search to do the finding
The question is not a hard one, but the reasoning behind it need a bit more thinking.
Implementation
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sorted(x - y for x, y in zip(nums1, nums2))
        ans, n = 0, len(diff)
        for i, x in enumerate(diff):
            idx = bisect_right(diff, -x, i+1)
            ans += n - idx
        return ans
----------------------------------------------------

	class Solution:
		def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
			diff = [(nums1[i] - nums2[i]) for i in range(len(nums1))]

			diff.sort()

			n = len(diff)
			eles = 0
			for i in range(n):
				if diff[i] <= 0:
					continue
				j = bisect_left(diff, -diff[i] + 1)
				eles += i - j
			return eles
    
----------------------------------------------------

Calculated the diffs array for each index in nums1 and nums2. Then, the problem converted to find the number of the pairs (i, j) in diffs where diffs[i] + diffs[j] > 0. Use sort and two pointers technique to solve it. Here is my code:

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diffs = sorted([n1 - n2 for n1, n2 in zip(nums1, nums2)])
        
        left, right, res = 0, len(nums) - 1, 0
        while left < right:
            if diffs[left] + diffs[right] > 0:
                # diffs[i] + diffs[right] > 0, where left <= i < right
                res += right - left
                right -= 1
            else:
                left += 1
        return res
      
      
      
