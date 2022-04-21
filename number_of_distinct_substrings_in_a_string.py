'''
Given a string s, return the number of distinct substrings of s.

A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.

 

Example 1:

Input: s = "aabbaba"
Output: 21
Explanation: The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
Example 2:

Input: s = "abcdefg"
Output: 28
'''

class Solution:
    def countDistinct(self, s: str) -> int:
        trie = {}
        res = 0
    
        for i in range(len(s)):
            node = trie
            for j in range(i, len(s)):
                if s[j] not in node:
                    node[s[j]] = {'end': True}
                
                node = node[s[j]]
                
                if node['end'] == True:
                    node['end'] = False
                    res += 1
                    
        return res
--------------------------------------------------

class Solution:
    def countDistinct(self, s: str) -> int:
        suffix = []
        
        for i in range(len(s)):
            suffix.append(s[i:])
        suffix.sort()
        def diff(s1,s2):
            i = 0
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                i+=1
            return i
        summ = 0
        for i in range(1, len(suffix)):
            summ += diff(suffix[i-1], suffix[i])
        return int((len(s)*(len(s) + 1)) /2) - summ
-------------------------------------------------------------

Time O(N^2)
Space O(N^2)

try to put all possible substrings of s into a trie and count them when we first time see them. Here is my code:

Trie = lambda: collections.defaultdict(Trie)
class Solution:
    def countDistinct(self, s: str) -> int:
        trie, res = Trie(), 0
        for i in range(len(s)):
            node = trie
            for j in range(i, len(s)):
                res += s[j] not in node
                node = node[s[j]]
        return res
      
      
