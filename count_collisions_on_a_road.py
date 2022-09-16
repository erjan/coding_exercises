'''
There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:

When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of collisions increases by 1.
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.
'''

class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        # At the beginning, leftest car can go without collide
        # At the beginning, rightest car can go without collide
        
        leftc = rightc = 0
        
        for c in directions:
            # if left side, no car stop or right answer + 0
            # if left side start to have car go right or stop
            # then cars after that are bound to be stopped so answer + 1
            if c == "L":
                ans += leftc
            else:
                leftc = 1
                
        for c in directions[::-1]:
            # if right side, no car stop or left answer + 0
            # if right side start to have car go left or stop
            # then cars after that are bound to be stopped so answer + 1
            if c == "R":
                ans += rightc
            else:
                rightc = 1
       
        return ans
      
       return len(directions.lstrip('L').rstrip('R').replace('S',''))
