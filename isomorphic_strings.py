'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = dict()
        t2s = dict()

        for i in range(len(s)):

            if s[i] not in s2t:

                s2t[s[i]] = t[i]
            elif s[i] in s2t:
                if s2t[s[i]] != t[i]:
                    print('bad')
                    return False

            if t[i] not in t2s:
                t2s[t[i]] = s[i]

            elif t[i] in t2s:
                if t2s[t[i]] != s[i]:
                    print('bad')
                    return False
        print('good')
        return True

    
#follow-up question :) from google - got this from discussions
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.string_to_int(s) == self.string_to_int(t)
        
    def string_to_int(self, s):
        output = []
        count = 0
        cache = defaultdict(int)
        
        for char in s:
            if char in cache:
                output.append(cache[char])
            else:
                output.append(count)
                cache[char] = count
                count += 1
                
        return tuple(output)
    
    def group_isomorphic(self, strings = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']):
        results = defaultdict(list)
        
        for string in strings:
            res = self.string_to_int(string)
            results[res].append(string)
        
        return results
