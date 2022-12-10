'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
'''

class Solution:
	def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
		wordSet = set(words)
		res = set()

		def dfs(s):
			if not s: 
				return True

			for i in range(len(s)):
				if s[:i + 1] in wordSet:           
					if dfs(s[i + 1:]): 
						return True

			return False

		for word in wordSet:
			wordSet.remove(word)                        # We need to not match the word with itself

			if dfs(word): 
				res.add(word)

			wordSet.add(word)

		return res

-----------------------------------------------------------------------------------------------------------
  class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = dict()
        mem = set(words)

        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
        
            cur["*"] = w
        
        def helper(w, level):
            cur = trie
            for i, c in enumerate(w):
                if c not in cur:
                    return False 

                cur = cur[c]

                if "*" in cur:
                    if i == len(w) - 1:
                        return level > 1
                    else:
                        if w[i + 1:] in mem or helper(w[i + 1:], level + 1):
                            return True

            return False

        
        ans = list()
        for w in words:
            if helper(w, 1):
                ans.append(w)
        
        return ans
