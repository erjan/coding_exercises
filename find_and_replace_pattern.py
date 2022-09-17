'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
'''

class Solution:
	def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
		def find(w): # function thats calculate the numeric pattern
			l = []
			m = defaultdict(int)
			i = 0
			for c in w:
				if c in m:
					l.append(m[c])
				else:
					i+=1
					m[c]=i
					l.append(m[c])
			return l
		ans = []
		pfind = find(p)
		for w in words:
			wfind = find(w)
			if wfind == pfind: ans.append(w) #check if numeric pattern of pattern is equal to pattern of word 
		return ans
