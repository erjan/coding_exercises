'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        a = salary
        a.remove(min(a))
        a.remove(max(a))
        result =  sum(a)/len(a)
        return result
