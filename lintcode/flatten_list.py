#Given a list, each element in the list can be a list or an integer.Flatten it into a simply list with integers.


class Solution(object):
   
    def flatten(self, nestedList):
        # Write your code here

        def helper(S):

            if S == []:
                return S
            if isinstance(S[0], list):
                return helper(S[0]) + helper(S[1:])
            return S[:1] + helper(S[1:])

        res = helper(nestedList)
        return res
