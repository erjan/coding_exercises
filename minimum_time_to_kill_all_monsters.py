'''
You are given an integer array power where power[i] is the power of the ith monster.

You start with 0 mana points, and each day you increase your mana points by gain where gain initially is equal to 1.

Each day, after gaining gain mana, you can defeat a monster if your mana points are greater than or equal to the power of that monster. When you defeat a monster:

your mana points will be reset to 0, and
the value of gain increases by 1.
Return the minimum number of days needed to defeat all the monsters.
'''



class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        power.sort()

        @cache
        def dp(mask: int, gain: int) -> int:
            if mask == (1 << n) - 1:
                return 0
            
            min_day = float('inf')
            for i in range(n):
                if mask & (1 << i):
                    continue
                min_day = min(min_day, dp(mask | (1 << i), gain + 1) + math.ceil(power[i] / gain))
            return min_day
        
        return dp(0, 1)
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        power.sort()

        @cache
        def dp(mask: int, gain: int) -> int:
            if mask == (1 << n) - 1:
                return 0
            
            min_day = float('inf')
            for i in range(n):
                if mask & (1 << i):
                    continue
                min_day = min(min_day, dp(mask | (1 << i), gain + 1) + math.ceil(power[i] / gain))
            return min_day
        
        return dp(0, 1)
