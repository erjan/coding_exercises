'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''

IDEA :
Firstly We have to find which algorithm or idea we can put in this question.
Determine in which direction question is flowing.

Binary search probably would not come to our mind when we first meet this problem. We might automatically treat weights as search space and then realize we've entered a dead end after wasting lots of time. In fact, we are looking for the minimal one among all feasible capacities.
We dig out the monotonicity of this problem: if we can successfully ship all packages within D days with capacity m, then we can definitely ship them all with any capacity larger than m. Now we can design a condition function, let's call it feasible, given an input capacity, it returns whether it's possible to ship all packages within D days. This can run in a greedy way: if there's still room for the current package, we put this package onto the conveyor belt, otherwise we wait for the next day to place this package. If the total days needed exceeds D, we return False, otherwise we return True.

Next, we need to initialize our boundary correctly. Obviously capacity should be at least max(weights), otherwise the conveyor belt couldn't ship the heaviest package. On the other hand, capacity need not be more than sum(weights), because then we can ship all packages in just one day.

Implementation :
'''

class Solution:
def shipWithinDays(self, weights: List[int], D: int) -> int:
    
    def feasible(capacity):
        days = 1
        local = 0
        for w in weights:
            local+=w
            if local>capacity:
                local = w
                days+=1
                if days>D:
                    return False
        return True
            
                
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right-left)//2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
            
    return left
