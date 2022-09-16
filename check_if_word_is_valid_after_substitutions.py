'''
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i == 'a':stack.append(i)
            elif i=='b':
                if not stack:return False
                else:
                    if stack[-1]=='a':stack.pop()
                    else:return False
                    stack.append(i)
            else:
                if not stack:return False
                else:
                    if stack[-1]=='b':stack.pop()
                    else:return False

        return len(stack)==0
        
-----------------------------------------------------------
class Solution:
    def isValid(self, S: str) -> bool:

	while S.count('abc'):
		S = S.replace('abc','')

	return not S
