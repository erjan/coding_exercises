'''
Some robots are standing on an infinite number line with their initial coordinates given by a 0-indexed integer array nums and will start moving once given the command to move. The robots will move a unit distance each second.

You are given a string s denoting the direction in which robots will move on command. 'L' means the robot will move towards the left side or negative side of the number line, whereas 'R' means the robot will move towards the right side or positive side of the number line.

If two robots collide, they will start moving in opposite directions.

Return the sum of distances between all the pairs of robots d seconds after the command. Since the sum can be very large, return it modulo 109 + 7.

Note:

For two robots at the index i and j, pair (i,j) and pair (j,i) are considered the same pair.
When robots collide, they instantly change their directions without wasting any time.
Collision happens when two robots share the same place in a moment.
For example, if a robot is positioned in 0 going to the right and another is positioned in 2 going to the left, the next second they'll be both in 1 and they will change direction and the next second the first one will be in 0, heading left, and another will be in 2, heading right.
For example, if a robot is positioned in 0 going to the right and another is positioned in 1 going to the left, the next second the first one will be in 0, heading left, and another will be in 1, heading right.

'''


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n, m = len(nums), int(1e9 + 7)
        # Ignore the Collisions
        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else: 
                nums[i] += d
        
        # Sort according to position to calculate abs sum of each pair in O(N)
        nums.sort()

        pre = nums.copy()
        # Calculate Prefix Sum
        for i in range(1, n):
            pre[i] += pre[i - 1]
            pre[i] %= m

        ans = 0
        for i in range(1, n):
            # each jth index contributes to j * nums[j] - pre[j - 1]
            ans += i * nums[i] - pre[i - 1]
            ans %= m
        return ans
