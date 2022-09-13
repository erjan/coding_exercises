'''
There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.
'''

class Solution:
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return abs(x)


    def mirrorReflection(self, p: int, q: int) -> int:
        time_for_reflection = self.lcm(p, q)
        is_right_side = True if time_for_reflection/q % 2 == 1 else False
        is_top_side = True if time_for_reflection/p % 2 == 1 else False

        if is_right_side and is_top_side:
            return 1
        elif not is_right_side and is_top_side:
            return 2
            
        return 0
--------------------------------------------------------------------------------
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
       
	   def step(right, up, distance):
            if distance == p:
                return 1 if (up and right) else 2 if up else 0
            elif distance > p:
                return step(not right, not up, distance % p)
            else:
                return step(not right, up, distance+q)
        
        return step(True, True, q)
