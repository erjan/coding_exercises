You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

-------------------------

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums

  
        if (a+b)<=c or(b+c)<=a or (c+a)<=b:
            return 'none'
        if a==b==c:
            return 'equilateral'
      
        elif a==b or b==c or c == a:
            return 'isosceles'
        elif a!=b and b!=c and c!=a:
            return 'scalene'            
-------------------------------------------------------------------

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2]>=nums[0]+nums[1]: return "none"
        if nums[0]==nums[2]: return "equilateral"
        if nums[0]==nums[1] or nums[1]==nums[2]: return "isosceles"
        return "scalene"
