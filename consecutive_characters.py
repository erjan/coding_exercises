'''
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 '''

class Solution:
    def maxPower(self, s: str) -> int:
        def f(x): return [list(group) for c, group in itertools.groupby(x)]

        s = f(s)

        maxi = 0
        for i in range(len(s)):

            if len(s[i]) > maxi:
                maxi = len(s[i])
        print(maxi)
        return maxi

       
#more classical solution

class Solution:
    def maxPower(self, s: str) -> int:
        
        # the minimum value for consecutive is 1
        local_max, global_max = 1, 1
        
        # dummy char for initialization
        prev = '#'
        for char in s:
            
            if char == prev:
                
                # keeps consecutive, update local max
                local_max += 1
                
                # update global max length with latest one
                global_max = max( global_max, local_max )
                
            else:
                
                # lastest consective chars stops, reset local max
                local_max = 1
            
                # update previous char as current char for next iteration
                prev = char
        
        
        return global_max
