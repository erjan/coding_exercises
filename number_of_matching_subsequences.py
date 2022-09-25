'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
'''



class Solution:
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    
    def is_sub(word):
        index=-1
        for ch in word:
            index=s.find(ch,index+1)
            if index==-1:
                return False
        return True
    
    c=0
    for word in words:
        if is_sub(word):
            c+=1
    
    return c
  
-------------------------------------------------------------------------------------------------------------------------
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans, mappings = 0, defaultdict(list)
        for index, char in enumerate(s):
            mappings[char].append(index)
        for word in words:
            prev, found = -1, True
            for c in word:
                tmp = bisect.bisect(mappings[c], prev)
                if tmp == len(mappings[c]): 
                    found = False
                    break
                else: prev = mappings[c][tmp]
            ans += found == True
        return ans
      
-----------------------------------------------------
	class Solution:  # The plan is to iterate through the words and, for each word w, move 
                     # letter by letter of w though the string s if possible to determine 
                     # whether w is a subsequence of s. If so, we  add to ans.
                     #
                     # We use a function and a cache because many of the words share letter
                     # sequences.

    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
                                    
        @lru_cache(None)            
        def checkWord(word):
            start = 0 

            for ch in word:         
                start = s.find(ch, start) + 1          # <-- find gives us the index of the
                if not start: return False             #     the next occurence of ch after
                                                       #     the index "start"
            return True
        
        return sum(checkWord(w) for w in words)        # <-- we count all the words that
                                                       #     returned True.
