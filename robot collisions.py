There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.
-----------------------------------------------------------------------------------------------------------------------
  class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        n = len(positions)
        robots =[ [ positions[ind], healths[ind], directions[ind], ind ] for ind in range(n)]
        robots.sort()
        for robot in robots:
            if robot[2] == 'R' or not stack or stack[-1][2] == 'L':
                stack.append(robot)
                continue
            
            if robot[2] == 'L':
                add = True
                while stack and stack[-1][2] == 'R' and add:
                    last_health = stack[-1][1]
                    if robot[1]> last_health:
                        stack.pop()
                        robot[1] -=1
                    elif robot[1]< last_health:
                        stack[-1][1] -=1
                        add=False
                    else:
                        stack.pop()
                        add=False
                if add:
                    stack.append(robot)
        
        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]
