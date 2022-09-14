'''
You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

 
 '''


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        max_chunk_sz = n // k
        
        d = collections.Counter(s)
        chars = sorted([c for c in d if d[c] >= k], reverse=True)
        if not chars:
            return ''
        
        old_cand = chars
        for m in range(2, max_chunk_sz+1):
            new_cand = []
            for t in self.get_next_level(old_cand, chars):
                if self.find(s, t*k):
                    new_cand.append(t)
            
            if len(new_cand) == 0:
                break
            old_cand = new_cand
        return old_cand[0]
        
    def get_next_level(self, cand, chars):
        for s in cand:
            for ch in chars:
                yield s + ch
        
    def find(self, s, t):
        # find subsequence t in s
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j += 1
            if j == len(t):
                return True
        return False
--------------------------------------------------------------------------
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # seq * k is a subsequent 
        counter = Counter(s)
        s = ''.join([c for c in s if counter[c] >= k])
        
        def is_subsequence(t):
            # determine that t is a subsequence of s
            i = j = 0
            while i < len(t) and j < len(s):
                if s[j] == t[i]:
                    i += 1
                    j += 1
                    
                else:
                    j += 1
            return i == len(t) and j <= len(s)
        
        def get_sequence(seqs, length):
            # if length > len(s) // k + 2:
            #     return seqs
            
            rslt = {}
            for seq, index in seqs.items():
                visited = set()
                i = index + 1
                while i < len(s):
                    newseq = (seq[:] + s[i])
                    if newseq not in visited:
                        if is_subsequence(newseq * k):
                            rslt[newseq] = i
                        visited.add(newseq)
                    i += 1
            
            if rslt:
                return get_sequence(rslt, length + 1)
            else:
                return seqs
        
        seqs = get_sequence({'': -1}, 0)
        # sort and return the biggest
        return sorted(list(seqs.keys()), key=lambda x: (len(x), x))[-1]
      
