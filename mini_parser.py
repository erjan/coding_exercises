'''
Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.
'''

class Solution:
    """
    we can approach this problem using stack
    """
    
    def dfs(self, i, s):
        res = NestedInteger()
        while i < len(s):
            if s[i] == '[':
                y, i = self.dfs(i+1, s)
                res.add(y)
            elif i < len(s) and s[i] == ']':
                i+=1
                return res, i
            elif i < len(s) and s[i] == ',':
                i+=1
            else: 
                if i < len(s):
                    start = i
                    while s[i] != ',' and s[i] != ']':
                        i+=1
                    res.add(NestedInteger(int(s[start:i])))
        return res, i
    
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] == '[':
            res, i = self.dfs(1, s)
            return res
        else:
            num = int(s)
            res = NestedInteger()
            res.setInteger(num)
            return res
