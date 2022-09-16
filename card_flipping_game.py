'''
You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.

Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.
'''

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        O(n) time complexity: n is length of fronts
        O(n) space complexity
        """
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        res = 9999
        for i in range(len(fronts)):
            if fronts[i] not in same: res = min(res, fronts[i])
            if backs[i] not in same: res = min(res, backs[i])
        return res % 9999
      
---------------------------------------------------------

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {ff for ff, bb in zip(fronts, backs) if ff == bb}
        return min((x for x in fronts+backs if x not in same), default=0)
