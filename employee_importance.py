'''
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
'''

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp):
            imp = emps[emp].importance            
            for s in emps[emp].subordinates:
                imp += dfs(s)
            return imp
        
        emps= {emp.id: emp for emp in employees}
        
        return dfs(id)
      
---------------------------------------------

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        id_to_emp = {employee.id: employee for employee in employees}
        importance = 0
        stack = [id_to_emp[id]]
        while stack:
            cur_emp = stack.pop()
            importance += cur_emp.importance
            stack.extend([id_to_emp[new_emp] for new_emp in cur_emp.subordinates])
        return importance 
