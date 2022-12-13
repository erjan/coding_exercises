'''
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.
'''

class Solution:
    def countOfAtoms(self, formula: str):
        # get the element count from the helper function
        formula_dict =  self.helper(formula)

        # build up the answer string by sorting the keys
        ans = ""
        for key in sorted(formula_dict):
            ans += key.strip()
            if formula_dict[key] > 1:
                ans += str(formula_dict[key])
                
        return ans

    def helper(self, formula: str):

        # initialize
        stack = []
        num = 0
        element = " "
        n = len(formula)

        i = 0
        while i < n:
            c = formula[i]

            # case 1: isalpha
            if c.isalpha():
                
                # is lower case:  append the char to the current element
                if c.islower():
                    element += c
                else:
                    # is upper case:  a new element
                    if len(element) > 1:
                        stack.append({element: 1})
                    
                    element = " " + c

            # case 2: is digit or ( )
            else:
                if len(element) > 1:
                    stack.append({element: 1})
                element = " "

                # is digit: increase the num of the last part in the stack
                if c.isdigit():
                    num = int(c)
                    while i < len(formula) - 1 and formula[i + 1].isdigit():
                        i += 1
                        c = formula[i]
                        num = 10 * num + int(c)
        
                    for key, value in stack[-1].items():
                        stack[-1][key] = value * num
                
                # enter recursion               
                elif c == "(":
                    part, j = self.helper(formula[i + 1:])
                    stack.append(part)
                    i = i + j
                elif c == ")":
                    # print("stack inner", stack)
                    return self.resolve_stack(stack), i + 1
            
            i += 1
        
        if len(element) > 1:
            stack.append({element: 1})
        
        # print("stack", stack)
        return self.resolve_stack(stack)

    def resolve_stack(self, stack):
        ret = {}
        for item in stack:
            for key,value in item.items():
                ret[key] = ret.get(key, 0) + value
        return ret
------------------------------------------------------------------------------------------
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        mp = {}
        stack = []
        for i, x in enumerate(formula): 
            if x == "(": stack.append(i)
            elif x == ")": mp[stack.pop()] = i
        
        def fn(lo, hi): 
            """Return count of atom in a freq table."""
            k = lo 
            ans = defaultdict(int)
            while k < hi: 
                cnt = 0 
                if formula[k] == "(": 
                    freq = fn(k+1, mp[k])
                    k = mp[k] + 1
                    while k < hi and formula[k].isdigit(): 
                        cnt = 10*cnt + int(formula[k])
                        k += 1
                    for key, val in freq.items(): ans[key] += val * max(1, cnt)
                else: 
                    atom = formula[k]
                    k += 1
                    while k < hi and formula[k] != "(" and not formula[k].isupper(): 
                        if formula[k].isalpha(): atom += formula[k]
                        else: cnt = 10*cnt + int(formula[k])
                        k += 1
                    ans[atom] += max(1, cnt)
            return ans 
        
        
        ans = []
        for k, v in sorted(fn(0, len(formula)).items()): 
            ans.append(k)
            if v > 1: ans.append(str(v))
        return "".join(ans)
      


