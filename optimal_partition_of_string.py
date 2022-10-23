'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
'''

class Solution:
    def partitionString(self, s: str) -> int:
        
        res = 1
        part = []
        part.append(s[0])
        s = list(s)
        for i in range(1, len(s)):

            if s[i] not in part:
                part.append(s[i])

            else:
                res += 1
                part = []
                part.append(s[i])

        print(res)
        return res
-----------------------------------------------------------------------------------------------
    # python greedy solution
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """        
        res = 0
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                seen.clear()
                res += 1
                seen.add(c)
        res += 1
        return res
      
----------------------------------------------------------------------------------------------------------------
class Solution:
    def partitionString(self, s: str) -> int:
        sub_set, ans = set(), 1
        for c in s:
            if c in sub_set:
                ans += 1
                sub_set = {c}
            else:
                sub_set.add(c)
        return ans
---------------------------------------------------------------------------------------------------
class Solution:
    def partitionString(self, s: str) -> int:

        def isUnique(s):
            return len(set(s)) == len(s)
			
		left = 0
        res = 0
        for right in range(1,len(s)+1):
            if not isUnique(s[left:right]):
                res += 1
                left = right-1
                
        return res+1 # don't forget there is still one partition we didn't add into res
-----------------------------------------------------------------------------------------------------------      
