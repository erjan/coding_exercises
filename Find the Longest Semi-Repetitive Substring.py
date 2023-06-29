'''
You are given a 0-indexed string s that consists of digits from 0 to 9.

A string t is called a semi-repetitive if there is at most one consecutive
pair of the same digits inside t. For example, 0010, 002020, 0123, 2002, and 
54944 are semi-repetitive while 00101022, and 1101234883 are not.

Return the length of the longest semi-repetitive substring inside s.

A substring is a contiguous non-empty sequence of characters within a string.
'''

--------------------------------------------------------------------------------------------------------------
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:


        def is_repet(subs):
            consec_pair = 0

            for i in range(len(subs)-1):
                if subs[i] == subs[i+1]:
                    consec_pair +=1
                elif subs[i] == subs[i+1] and consec_pair >= 1:
                    return False
            if consec_pair <=1:
                return True
            return False


        cur_len = 0
        n = len(s)
        for i in range(n):


            for j in range(i, n+1): #here is n+1 vs n

                substr = s[i:j]

                if is_repet(substr):
                    cur_len = max(len(substr), cur_len)
        return cur_len

-----------------------------------------------------------------------
#DP approach
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res=0
        tab=[1]
        for i in range(1,len(s)):
            if ( s[i]==s[i-1]):
                tab.append(1)
            else:
                tab[-1]=tab[-1]+1
        for j in range(1,len(tab)):
            res=max(res,tab[j]+tab[j-1])
        
        return max(res,tab[0])
                
                
        
