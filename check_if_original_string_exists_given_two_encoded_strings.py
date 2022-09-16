'''
An original string, consisting of lowercase English letters, can be encoded by the following steps:

Arbitrarily split it into a sequence of some number of non-empty substrings.
Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
Concatenate the sequence as the encoded string.
For example, one way to encode an original string "abcdefghijklmnop" might be:

Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes ["ab", "12", "1", "p"].
Concatenate the elements of the sequence to get the encoded string: "ab121p".
Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.
'''

class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
            find if s1 and s2
            sequence matter dp
            
            dp(ci, cj, diff):  return if s1 and s2 matches from location. ci,cj where diff represents previoius lefttoover from s1 or s2

            state ttransittion:
                look at code  for this, there are lott of ttransittiion
                
                
                
            base case
                ci and cj both at end, rett. true
                iif. one exhaused rertun False
        
        """
        
        """
        eex.
        
            internationalization
             ^
            i18n
             ^
             ci = 1
             cj = n
             
             ci = 18
             cj = n 
              we try both to see. which one. reaches the end
        """
        @cache
        def dp(ci, cj, diff):
            
            if ci == len(s1) and cj == len(s2) and diff == 0:
                return True
            
            if ci > len(s1) or cj > len(s2):
                return False
            
            
            if ci < len(s1) and s1[ci].isdigit():
                k = ci
                curr = ""
                while k < len(s1) and s1[k].isdigit():
                    curr += s1[k]
                    k += 1
                    if dp(k, cj, diff + int(curr)) == True:
                        return True
            elif cj < len(s2) and s2[cj].isdigit():
                k = cj
                curr = ""
                while k < len(s2)  and s2[k].isdigit():
                    curr += s2[k]
                    k += 1
                    if dp(ci, k, diff - int(curr)) == True:
                        return True
            elif diff == 0:
                if ci < len(s1) and cj < len(s2) and s1[ci] == s2[cj]:
                    return dp(ci+1, cj+1, diff)
                else:
                    return False
            else:
                if diff > 0 :
                    # s1 exist more
                    return dp(ci, cj+1, diff-1)
                else:
                    return dp(ci+1, cj, diff+1)
            
            return False
        
        return dp(0, 0, 0)
