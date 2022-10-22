'''
You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge.The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

'''

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [] 
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])  #note that this can be a float
        time.sort() #create time of arrival table, and sort it. we just greedily kill the monster that will arrive first

        for t in range(len(time)): #t is also the current time
            monster_has_arrived = (time[t] - t <= 0)
            if monster_has_arrived : 
                return t #we can just return the current time, which is also the number of monster we have killed, because we can only eliminate one monster per timestep
            
        return len(time) #we killed all monsters
      
---------------------------------------------------------------------------------------
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        time = []
        
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        
        time.sort()
        
        for t in range(len(time)):
            
            monster_arrived =(time[t]-t<=0)
            
            if monster_arrived:
                return t
        return len(time)
      
