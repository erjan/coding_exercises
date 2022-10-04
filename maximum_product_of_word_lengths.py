'''
Given a string array words, return the maximum value of
length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
'''






Bit Mask
This approach replaces the char_set in above approach using a bit_mask. The set bits of the bit_mask will indicate the presence of a char in the word. This will also help improve the time complexity as the code will replace the & of two hashset which is O(min(len(s1), len(s2)) with & operation between two integers which is O(1).

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        
        bit_masks = [0] * n
        lengths = [0] * n
        
        for i in range(n):             
            for c in words[i]:
                bit_masks[i]|=1<<(ord(c) - ord('a')) # set the character bit            
            lengths[i]=len(words[i])
                        
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (bit_masks[i] & bit_masks[j]):
                    max_val=max(max_val, lengths[i] * lengths[j])
        
        return max_val  
        
-----------------------------------------------------------------------------------------------------
Hashset
The approach is quite straightforward. We do the following:

Compute the unique char_set in one iteration.
Find all the pairs and compute the max product only if there are no common characters between two char_sets. In python, you can use & operator which serves as the intersection operator.
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)                        
        char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (char_set[i] & char_set[j]): # if nothing common
                    max_val=max(max_val, len(words[i]) * len(words[j]))
        
        return max_val 
        
------------------------------------------------------------------------------------------------------------------------
def maxProduct(self, words: List[str]) -> int:
	def common(chars1, chars2):
		for c1, c2 in zip(chars1, chars2):
			if c1 and c2: return True
		return False
	chars, ans = [[False]*26 for i in range(len(words))], 0
	for i, word in enumerate(words):
		for ch in word:
			chars[i][ord(ch) - ord('a')] = True
		for j in range(i):
			if not common(chars[i], chars[j]):
				ans = max(ans, len(words[i]) * len(words[j]))
	return ans
