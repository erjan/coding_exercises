'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''



'''
Left asteroid destroys right asteroid: abs(left) > abs(right) - nothing to pop off the stack, we just move on to considering the next asteroid
Both asteroids destroyed: abs(left) == abs(right) - pop off the stack the top of the stack asteroid as it just got destroyed, but also move on as the considered asteroid has just been destroyed too
Right asteroid destroys left asteroid: abs(left) < abs(right) - pop off the top of the stack asteroid as it just got destroyed, but don't move on - this asteroid could destroy the new top of the stack asteroid!
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
			# if there's things on the stack, we need to consider if we've got case 4
            while stack and stack[-1] > 0 and asteroid < 0:
				# determine which asteroids are exploding
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
					# considered asteroid might still destroy others so continue checking
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
			# if nothing on the stack, or cases 1-3, just append
            else:
                stack.append(asteroid)
        return stack
