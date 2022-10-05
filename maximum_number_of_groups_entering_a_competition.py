'''
You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:

The sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).
The total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).
Return the maximum number of groups that can be formed.
'''

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        sortedGrades = sorted(grades)

        groupNums = 0
        total = 0
        while total <= len(sortedGrades):
            groupNums += 1
            total += groupNums
        return groupNums - 1
      
----------------------------------------------------------------
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        x = len(grades)
        n = 0.5 * ((8 * x + 1) ** 0.5 - 1)
        ans = int(n)
        
        return ans
