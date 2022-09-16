'''
The hash of a 0-indexed string s of length k, given integers p and m, is computed using the following function:

hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
Where val(s[i]) represents the index of s[i] in the alphabet from val('a') = 1 to val('z') = 26.

You are given a string s and the integers power, modulo, k, and hashValue. Return sub, the first substring of s of length k such that hash(sub, power, modulo) == hashValue.

The test cases will be generated such that an answer always exists.

A substring is a contiguous non-empty sequence of characters within a string.
'''
Intuition
Good time to learn rolling hash.
what's hash?
The definition hash(s, p, m) in the description is the hash of string s based on p.

what's rolling hash?
The hash of substring is a sliding window.
So the basis of rolling hash is sliding window.

Explanation
Calculate the rolling hash backward.
In this process, we slide a window of size k from the end to the begin.

Firstly calculate the substring hash of the last k characters,
then we add one previous backward and drop the last characters.

Why traverse from end instead of front?
Because cur is reminder by mod m,
cur = cur * p works easier.
cur = cur / p doesn'r work easily.

---------------------------------------------------------------------------
    def subStrHash(self, s, p, m, k, hashValue):
        def val(c):
            return ord(c) - ord('a') + 1
            
        res = n = len(s)
        pk = pow(p,k,m)
        cur = 0

        for i in xrange(n - 1, -1, -1):
            cur = (cur * p + val(s[i])) % m
            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % m
            if cur == hashValue:
                res = i
        return s[res: res + k]
      
----------------------------------------------------------------------------------------------
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powSoFar = 1        
        total = ord(s[0]) - ord('a') + 1
        for idx in range(1, k):
            powSoFar *= power
            total += ((ord(s[idx]) - ord('a')) + 1) * (powSoFar)
        
        #print(total)
        if (total % modulo) == hashValue:
            return s[:k]
        
        for idx in range(k, len(s)):
            total = total - ((ord(s[idx - k]) - ord('a')) + 1)
            #print(total)
            total = total // power
            #print(total)
            total = total + (((ord(s[idx]) - ord('a')) + 1) * powSoFar)
            #print(total)
            
            if (total % modulo) == hashValue:
                return s[(idx - k + 1) : (idx + 1)]
        
        return ""
