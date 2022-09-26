'''
You are given an array of strings equations that represent relationships 
between variables where each string equations[i] is of length 4 and takes one of two 
different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
'''

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {chr(num):chr(num) for num in range(ord("a"), ord("z")+1)}
        
        def find(val):
            if parents[val] == val:
                return val
            parents[val] = find(parents[val])
            return parents[val]
        
        for x,sign,_,y in equations:
            if sign == "=":
                parent_x, parent_y = find(x), find(y)
                parents[parent_x] = parent_y
        
        for x,sign,_,y in equations:
            if sign == "!" and find(x) == find(y):
                return False
        
        return True
