'''
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.
'''

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        firstCanBreak, secondCanBreak = False, False
        for idx in range(len(s1)-1,-1,-1):
            if s1[idx] == s2[idx]:
                continue
            elif s1[idx] > s2[idx]:
                firstCanBreak = True
            elif s2[idx] > s1[idx]:
                secondCanBreak = True
            if secondCanBreak == firstCanBreak:
                return False
        return True
      
----------------------------------------------------------------------
def checkIfCanBreak(self, s1: str, s2: str) -> bool:
	s1 = sorted(s1)
	s2 = sorted(s2)
	a1 = a2 = True
	for i in range(len(s1)):
		if(s1[i] < s2[i]):
			a1 = False
		elif(s1[i] > s2[i]):
			a2 = False
	return a1 or a2

--------------------------------------------------------------------------------------
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1, s2 = sorted(s1), sorted(s2)
        
        first = all([s1[i] >= s2[i] for i,_ in enumerate(s1)])
        
        return first if first else all([s1[i] <= s2[i] for i,_ in enumerate(s1)])
      
---------------------------------------------------------------------------------------------------------- 

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1, s2 = sorted(s1), sorted(s2)
        
        
        n = len(s1)
        
        first = sec = True
        
        for i in range(n):
            
            if s1[i] < s2[i]:
                first = False
            if s1[i] > s2[i]:
                sec = False
        
        return first or sec
                
            
