'''
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
'''

def minFlips(self, s: str) -> int:
        # Minimum number of flips to return
        minimumFlips = len(s)
        
        # Window Size
        k = len(s)
        
        # For strings of odd length, double them
        # So that we do not have to manually perform type-1 operation 
        # that is, taking each bit and moving to end of string
        s = s if k % 2 == 0 else s + s
        
        # There can be only two valid alternating strings as we only have 0 and 1
        # One starts with 0 and other with 1
        # e.g. for a string of length 3 we can have either 010 or 101
        altArr1, altArr2 = [], []        
        for i in range(len(s)):
            altArr1.append("0" if i % 2 == 0 else "1")
            altArr2.append("1" if i % 2 == 0 else "0")
            
        alt1 = "".join(altArr1)
        alt2 = "".join(altArr2)
        
        
        # Minimum Number of operations = Minimum Difference between the string and alt2 and alt3
        diff1, diff2 = 0,0
        
        # Sliding Window Template Begins
        i,j = 0,0
        
        
        while j < len(s):
            if s[j] != alt1[j] : diff1 += 1
            if s[j] != alt2[j] : diff2 += 1
                
            if j - i + 1 < k: j += 1
            else:
                minimumFlips = min(minimumFlips, diff1, diff2)
                if s[i] != alt1[i] : diff1 -= 1
                if s[i] != alt2[i] : diff2 -= 1
                i += 1
                j += 1
        
        return minimumFlips
      
-------------------------------------------------------------------------------------------------------

class Solution(object):
    def minFlips(self, s):
        n=len(s) # we save this length as it is length of window
        s+=s #we add this string because we can have any possibility like s[0]->s[n-1] or s[2]->s[n+1]meaning is that any continous variation with n length ... 
        ans=sys.maxint #assiging the answer max possible value as want our answer to be minimum so while comparing min answer will be given 
        ans1,ans2=0,0#two answer variables telling amount of changes we require to make it alternative
        s1=""#dummy string like 10010101
        s2=""#dummy string like 01010101
        for i in range(len(s)):
            if i%2==0:
                s1+="1"
                s2+="0"
            else :
                s1+="0"
                s2+="1"
        for i in range(len(s)):
            if s[i]!=s1[i]:#if they dont match we want a change so ++1
                ans1+=1
            if s[i]!=s2[i]:
                ans2+=1
            
            if i>=n:
                if s[i-n]!=s1[i-n]:#now we have gone ahead so removing the intial element but wait if that element needed a change we added ++ earlier but now he is not our part so why we have his ++ so to nullify its ++ we did a -- in string
                    ans1-=1
                if s[i-n]!=s2[i-n]:
                    ans2-=1
            if i>=n-1#when i reaches n-1 we have n length so we check answer first time and after that we always keep seeing if we get a less answer value and after the loop we get 
                ans=min([ans,ans1,ans2])
        return ans          
      
-----------------------------------------------------------------------------------------      
#dp
class Solution:
    def minFlips(self, s: str) -> int:
        prev = 0
        start_1, start_0, start_1_odd, start_0_odd = 0,0,sys.maxsize,sys.maxsize
        odd = len(s)%2
        for val in s:
            val = int(val)
            if val == prev:
                if odd:
                    start_0_odd = min(start_0_odd, start_1)
                    start_1_odd += 1
                start_1 += 1
            else:
                if odd:
                    start_1_odd = min(start_1_odd, start_0)
                    start_0_odd += 1
                start_0 += 1
            prev = 1 - prev
        return min([start_1, start_0, start_1_odd, start_0_odd])
