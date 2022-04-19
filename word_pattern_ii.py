'''

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
'''


Use dictionary to store patterns, and backtrack when mismatch happens.

def wordPatternMatch(self, pattern, str):
    return self.dfs(pattern, str, {})

def dfs(self, pattern, str, dict):
    if len(pattern) == 0 and len(str) > 0:
        return False
    if len(pattern) == len(str) == 0:
        return True
    for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
        if pattern[0] not in dict and str[:end] not in dict.values():
            dict[pattern[0]] = str[:end]
            if self.dfs(pattern[1:], str[end:], dict):
                return True
            del dict[pattern[0]]
        elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
            if self.dfs(pattern[1:], str[end:], dict):
                return True
    return False
--------------------------------------------------------------
def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(cur: str, pattern: str, mappings: dict):
            # if the pattern is empty, we've exhausted our search
            if not pattern:
                # if the string is also empty, we've found a bijective mapping
                return not cur
            # if the pattern is already mapped, we must use the provided mapping
            if pattern[0] in mappings:
                # if this isn't a valid mapping, return false
                if cur[:len(mappings[pattern[0]])] != mappings[pattern[0]]:
                    return False
                # otherwise continue backtracking
                return backtrack(cur[len(mappings[pattern[0]]):], pattern[1:], mappings)
            # try each subset of the remaining string as a mapping
            for i in range(len(cur)):
                # if the current substring maps to another value, it isn't valid
                if cur[:i+1] in mappings.values():
                    continue
                # map the pattern to the substring
                mappings[pattern[0]] = cur[:i+1]
                # backtrack
                if backtrack(cur[i+1:], pattern[1:], mappings):
                    return True
                # delete the invalid mapping
                del mappings[pattern[0]]
            # none of the substrings were valid, so there is no valid mapping
            return False
        return backtrack(s, pattern, {})
      
-------------------------------------------------------------------------------------
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        chars = list({c: 0 for c in pattern})
        ctoi = {c: idx for idx, c in enumerate(chars)}

        def solve(i, mapping, inverse):
            if len(mapping) == len(chars):
                return "".join(mapping[ctoi[c]] for c in pattern) == s

            substr = ""
            for idx in range(i, len(s)):
                substr += s[idx]
                if substr not in inverse:
                    if solve(idx + 1, [*mapping, substr], inverse | {substr}):
                        return True
            return False

        return solve(0, [], set())
Map every substring starting from an offset into s to the next unique letter in pattern.
Skip over substrings which have already been mapped.
When all unique letters in pattern are mapped, check if they combine to form s.
Note: I use a dictionary instead of a set in chars to get unique characters in pattern so as to preserve their order. This is important.
  
-------------------------------------------------------------------------------------------------
Intuition
The scale of the input is very small ([1,20]), we can do a brute force solution, which is bacailly try out all possible combinations and see whether there is any fit.
Take advantage of itertools in Python
This question is basically following two questions add up together.
Find combinations given a list of values:
77. Combinations
Given a list of words, check if the given pattern matches the words:
290. Word Pattern
Most of solutions you see in the discuss session is merging the backtracking of combinations and the process of matching pattern together. This solution seperated them to make it easier to understand.

Implementation
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        lp, ls = len(pattern), len(s)
        for nums in itertools.combinations(range(1, ls), lp-1):
            p_to_word, word_to_p, prev = dict(), dict(), 0
            nums += (ls,)
            for i in range(lp):
                if pattern[i] in p_to_word and p_to_word[pattern[i]] != s[prev:nums[i]] or \
                s[prev:nums[i]] in word_to_p and word_to_p[s[prev:nums[i]]] != pattern[i]:
                    break
                else:    
                    p_to_word[pattern[i]] = s[prev:nums[i]]
                    word_to_p[s[prev:nums[i]]] = pattern[i]
                prev = nums[i]
            else:
                return True
        return False
      
--------------------------------------------------------------------------------------------------
Each letter in the pattern maps to a substring in the original string. We need to look at all combinations of mapping. This means we need to go ahead with backtracking as we are looking at all possible combinations.

We need hash_map to store the pattern mapping. A set to store the existing patterns and a memo to store which of the cases are not working.

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        hash_map = {}
        memo = set()
        existing_patterns = set()
        def dfs(i, idx):
            if (i, idx) in memo:
                return False
            if i == len(pattern) and idx == len(s):
                return True
            if i >= len(pattern) or idx >= len(s):
                return False
            if pattern[i] in hash_map:
                registered = hash_map[pattern[i]]
                for k in range(len(registered)):
                    if (idx + k == len(s)) or (registered[k] != s[idx + k]):
                        return False
                return dfs(i+1, idx + len(registered))
            
            for k in range(idx, len(s)):
                curr_pattern = s[idx:k+1]
                if curr_pattern not in existing_patterns: # check if current pattern is already present
                    existing_patterns.add(curr_pattern)
                    hash_map[pattern[i]] = s[idx:k+1] # store the pattern in hashmap
                    if dfs(i+1, k+1):
                        return True
                    del hash_map[pattern[i]] # backtrack
                    existing_patterns.remove(curr_pattern) #backtrack
                else:
                    continue    # if current pattern is already present in the set of existing patterns then continue
                
        return dfs(0, 0)
      
  
      
  
