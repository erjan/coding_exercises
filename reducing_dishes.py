'''
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
'''


class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        arr = [0] + sorted(satisfaction)
        return max( sum(num*factor for factor, num in enumerate(arr[i:]) ) for i in range(len(arr)) )
      
--------------------------------------------------------------------------------------------------------------
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        total, res = 0, 0
        for n in sorted(satisfaction, reverse=True):
            total += n
            if total > 0:
                res += total
        return res
