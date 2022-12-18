'''
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
'''

class Solution:
    def similarPairs(self, words: List[str]) -> int:

        res = 0
        for i in range(len(words)):

            w = set(words[i])

            for j in range(i+1, len(words)):
                w2 = set(words[j])
                if w == w2:
                    res+=1
        
        return res
      
-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution: 
	def similarPairs(self, words: List[str]) -> int: 
		ans = 0
		freq = Counter()
		for word in words: 
			mask = reduce(or_, (1<<ord(ch)-97 for ch in word))
			ans += freq[mask]
			freq[mask] += 1
		return ans
