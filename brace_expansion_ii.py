'''
Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.
'''

The general idea
Split expressions into groups separated by top level ','; for each top-level sub expression (substrings with braces), process it and add it to the corresponding group; finally combine the groups and sort.

Thought process
in each call of the function, try to remove one level of braces
maintain a list of groups separated by top level ','
when meets ',': create a new empty group as the current group
when meets '{': check whether current level is 0, if so, record the starting index of the sub expression;
always increase level by 1, no matter whether current level is 0
when meets '}': decrease level by 1; then check whether current level is 0, if so, recursively call braceExpansionII to get the set of words from expresion[start: end], where end is the current index (exclusive).
add the expanded word set to the current group
when meets a letter: check whether the current level is 0, if so, add [letter] to the current group
base case: when there is no brace in the expression.
finally, after processing all sub expressions and collect all groups (seperated by ','), we initialize an empty word_set, and then iterate through all groups
for each group, find the product of the elements inside this group
compute the union of all groups
sort and return
note that itertools.product(*group) returns an iterator of tuples of characters, so we use''.join() to convert them to strings
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        word_set = set()
        for group in groups:
            word_set |= set(map(''.join, itertools.product(*group)))
        return sorted(word_set)
      
-------------------------------------------------------------------------------
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        s = list(reversed("{" + expression + "}"))
        
        def full_word(): 
            cur = [] 
            while s and s[-1].isalpha():    
                cur.append(s.pop())            
            return "".join(cur)
        
        def _expr(): 
            res = set()    
            if s[-1].isalpha(): 
                res.add(full_word())    
            elif s[-1] == "{":   
                s.pop() # remove open brace
                res.update(_expr()) 
                while s and s[-1] == ",": 
                    s.pop() # remove comma 
                    res.update(_expr())    
                s.pop() # remove close brace 
            while s and s[-1] not in "},": 
                res = {e + o for o in _expr() for e in res}
            return res    
        
        return sorted(_expr()) 
