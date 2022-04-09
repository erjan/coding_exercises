'''
You are given an array of strings strs. You could concatenate these strings together into a loop, where for each string, you could choose to reverse it or not. Among all the possible loops

Return the lexicographically largest string after cutting the loop, which will make the looped string into a regular one.

Specifically, to find the lexicographically largest string, you need to experience two phases:

Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
And your job is to find the lexicographically largest one among all the possible regular strings.

'''

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [max(x, x[::-1]) for x in strs]
        
        ans = ""
        for i in range(len(strs)): 
            rev = strs[i][::-1]
            rest = "".join(strs[i+1:] + strs[:i])
            for k in range(len(strs[i])): 
                ans = max(ans, strs[i][k:] + rest + strs[i][:k])
                ans = max(ans, rev[k:] + rest + rev[:k])
        return ans 
