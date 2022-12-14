'''
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.
'''

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions += [[1, 0]]
        restrictions.sort() #sort by building number

        #if last building is not in restriction add it
        #and its height must be <= n-1 because first building is 0
        if restrictions[-1][0] != n: restrictions.append([n, n-1])
        
        c = 1; c_h = 0
        for i in range(len(restrictions)):
            b,h = restrictions[i]

            if (b-c) + c_h < h:
                restrictions[i][1] = (b-c) + c_h
            else:
                c = b; c_h = h 
        
        c, c_h = restrictions[-1]
        for i in range(len(restrictions)-1, -1, -1):
            b,h = restrictions[i]

            if (c-b) + c_h < h:
                restrictions[i][1] = (c-b) + c_h
            else:
                c = b; c_h = h 
        
        ans = 0
        for i in range(len(restrictions) - 1):
            left, left_h = restrictions[i]
            right, right_h = restrictions[i+1]

            #y1 = (x - left) + left_h
            #y2 = (rigth - x) + right_h, their intersection is the max_h in that interval
            # x - left + l_h = right - x + r_h
            # x = (right + left + r_h - l_h)/2
            # y = (right + left + r_h - l_h)/2 - left + l_h
            location = (right + left + right_h - left_h)//2 #building_id must be integer
            height = location - left + left_h
            ans = max(ans, height)

        return ans
      
----------------------------------------------------------------------------------------------------
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        restrictions.append([1, 0])  # Add the restriction for the initial position
        restrictions.sort(key=lambda x: x[1] + x[0])  # Sort by increasing i + h
        idx = 0  # The index in the restrictions array
        max_height = 0
        while idx < len(restrictions):
            pos, h = restrictions[idx]
            idx += 1
            while idx < len(restrictions) and restrictions[idx][1] - restrictions[idx][0] >= h - pos:
				# skip the next restriction if it is "above" the line starting from the current one
                idx += 1
            if idx == len(restrictions):
				# Handles the last restriction: fill the line until the last position at n
                max_height = max(max_height, h + n - pos)
                break
            next_pos, next_h = restrictions[idx]
			# A bit of maths gives us the formula for the maximum height between two consecutive
			# restrictions
            max_height = max(max_height, (h + next_h + next_pos - pos) // 2)
        return max_height
