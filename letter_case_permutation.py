'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
'''


Iterative

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        output = [""]
        for ch in S:
            for i in range(len(output)):
                if ch.isalpha():
                    output.append(output[i]+ch.lower())
                    output[i] = output[i]+ch.upper()
                else:
                    output[i] = output[i]+ch
        return output
Recursive

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.helper(s, "", [])

    def helper(self, s: str, current: str, solution:List[str]) -> List[str]:
        if len(s)==0:
            solution.append(current)
            return solution
        if s[0].isalpha():
            self.helper(s[1:], current+s[0].lower(), solution)
            self.helper(s[1:], current+s[0].upper(), solution)
        else:
            self.helper(s[1:], current+s[0], solution)
        return solution
