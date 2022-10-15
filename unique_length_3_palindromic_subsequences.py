'''
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
'''


basicsally first stores all elements with indices
now for elment having twice occurence of more using the first and last occurnces and getting how many distinct characters are there in between this way u can form palindrom
if u like the way i solved do upvote it gives A Lot of motivation

class Solution(object):
    def countPalindromicSubsequence(self, s):
        d=defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
        ans=0
        for el in d:
            if len(d[el])<2:
                continue
            a=d[el][0]
            b=d[el][-1]
            ans+=len(set(s[a+1:b]))
        return(ans)
      
------------------------------------------------------------------------------------------------------------
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        elif len(s) == 3:
            return 1 if s[0]==s[2] else 0
                
        else:
            num_of_palindromes = 0
            unique = list(set(s))
            for char in unique:
                count = s.count(char)
                if count > 1:
                    # find first and last index of char in s
                    a_index = s.index(char)
                    c_index = s.rindex(char)
                    # find num of unique chars between the two indeces 
                    between = s[a_index+1:c_index]
                    num_of_palindromes += len(list(set(between)))
                
            return num_of_palindromes
      
