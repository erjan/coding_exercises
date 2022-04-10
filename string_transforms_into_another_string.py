'''
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.
'''

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # 0. if the strings are equal return True
        if str1 == str2:
            return True
        # 1. set up a hashmap to map str1 keys to str2 values, and a set to contain the characters in str2
        hashmap = {}
        unique = set()
        # 2. go thru each index in str1, and add it to the hashmap if it isn't in there. if it is, and doesn't match up with the previous value used for that str1[i] key then return False
        for i in range(len(str1)):
            if str1[i] not in hashmap:
                hashmap[str1[i]] = str2[i]
            else:
                if hashmap[str1[i]] != str2[i]:
                    return False
            # 3. add each str2[i] character to the unique hashset regardless
            unique.add(str2[i])
        # 4. check if there were under 26 unique values, if there are return True, if not, return False
        if len(unique) < 26:  # makes sure no character in str1 maps to 2 or more characters in str2
            return True
        return False
      
----------------------------

class Solution:
    def canConvert(self, str1, str2):
        h = {}
        
        n = len(str1)
        if len(str2) != n: return False
        if str1 == str2: return True
        
        for i in range(n):
            start, end = str1[i], str2[i]
            if start in h and h[start] != end:
                return False
            if start not in h:
                h[start] = end

        if len(h.keys()) == 26 and len(list(set(h.values()))) == 26:
            return False
            
        return True
