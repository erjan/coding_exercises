'''
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they 
are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and 
needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
'''


class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        n = len(position)

        def countBalls(d):
            n_balls, cur = 1, position[0]
            for i in range(1, n):
                if position[i]-cur >= d:
                    n_balls += 1
                    cur = position[i]
            return n_balls

        left = 1; right =  position[n-1]-position[0]
        
        while left <= right:
            mid = (left+right)//2
            if countBalls(mid) >= m:
                left = mid+1
            else:
                right = mid-1
        return right
      
---------------------------------------------------------   

This probelm is conceptually very similar to 1011. Capacity To Ship Packages Within D Days, where the monotonicity allowing us to use binary search takes the form of a step function/threshold.

Given a proposed distance x, we can easily check in O(n) time whether it is possible to distribute the balls so that the distance between each adjacent pair of balls is at least x. This can be done greedily by inserting a ball whenever we are at >= x distance away from the previous ball.

Now that we have a function to tell us if a solution is valid, all that is left to be done is to find the best solution (the threshold) among all solutions. This can be done efficiently using binary search once we hammer down the range of possible values to search. Low here is 1 since we cannot place two balls in the same busket. High here is (position[n-1]-position[0])/(m-1) since evenly spacing the balls is theoretically the best way to maximum distance between adjacent balls.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def verify(x):
            '''
            Returns true if we can put m balls in the buskets
            while maintining at least x distance between them
            '''
            count, prev = 1, position[0]
            for i in range(1, len(position)):
                if position[i]-prev >= x:
                    prev = position[i]
                    count += 1
            return count >= m
    
        position.sort()
        low, high, ret = 1, (position[-1]-position[0])//(m-1)+1, -1
        while low <= high:
            mid = low+(high-low)//2
            if verify(mid):
                # this is a solution but we are looking for the maximum
                # update ret and continue looking for a even larger one
                ret = mid
                low = mid+1
            else:
                high = mid-1
        return ret
