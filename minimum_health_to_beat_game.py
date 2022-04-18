
'''
You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array damage where damage[i] is the amount of health you will lose to complete the ith level.

You are also given an integer armor. You may use your armor ability at most once during the game on any level which will protect you from at most armor damage.

You must complete the levels in order and your health must be greater than 0 at all times to beat the game.

Return the minimum health you need to start with to beat the game.

 
 '''


You will only get one shot, so pick the turn that you may lose the most health
Your total loss-avoidable will be min(max(damage), armor)
You will need at least sum(damage) + 1 to pass the game without any armor
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(max(damage), armor)
      
      
---------------------------------------------
def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) - min(armor, max(damage)) + 1
  
  
---------------------------------------------------------
Explaination:
If you have 0 armor, you need sum(damage) + 1 health to survive against the damage.
Eg:

Sum of [12, 5, 6, 1, 4] = 28. So you need 28 + 1 = 29 health.
Armor can reduce upto "armor" damage.
Naturally you want to use your armor against the enemy's strongest attack.
There can be two scenarios here:

armor > max(damage) [eg: armor = 14]
armor <= max(damage) [eg: armor = 10]
If armor is greater, it will soak upto the amount of that damage (ie: 12) and the remaining discarded from further calculations. [reduction = 12]
If the damage is greater, net damage will be reduced by amount of armor (ie: 12 - 10 = 2). [reduction = 10]

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        top = max(damage)
        reduction = armor if top > armor else top
        return sum(damage) - reduction + 1
      
-----------------------------------------------------------------------
The main idea is to find the index of the maximum damage, then use the armor once to block this damage.
If the maximum damage is above the armor can resist, then at the stage, we need at least damage_i - armor + 1 health to survive, otherwise, just use the armor to completely block it.
The overall time complexity is O(n) and space complexity is O(1).
class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        max_damage = max(damage)
        target_index = 0
        for index, d in enumerate(damage):
            if d == max_damage:
                target_index = index 
                break
        
        ans = 1
        for index, d in enumerate(damage):
            if index == target_index:
                if armor >= d:
                    pass 
                
                else:
                    ans += d - armor 
                    
            else:
                ans += d
        
        return ans
      
-------------------------------------------------------------------------------
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        if not armor: return sum(damage) + 1
        
        def bs(health):            
            used = 0
            stack = [] # keep maximum heap
            for d in damage:
                if not used:
                    heappush(stack, -d)
                if d >= health:
                    # use the armor to maximize its effect (to counter previous maximum damage)
                    if not used and health - d + min(armor, -stack[0]) > 0:
                        health = health - d + min(armor, -stack[0])
                        used = 1
                    else:
                        return False
                else:
                    health -= d
            return True
        
        
        l, h = 1, sum(damage) + 1
        while l < h:
            mid = l + (h - l) // 2
            if bs(mid):
                h = mid
            else:
                l = mid + 1
        
        return l
                
        
-------------------------------------------------------------
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_val=max(damage)
        damage[damage.index(max_val)]-=min(armor, max_val)
        return sum(damage)+1
