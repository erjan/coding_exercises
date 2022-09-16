'''
You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.
'''

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counter_a = Counter(ord(ch) - ord('a') for ch in a)
        counter_b = Counter(ord(ch) - ord('a') for ch in b)
        # keys will go from 0 to 25
        
        # condition 3
        # min cost to turn a consisting of single character only is len(a) - max_freq_of_character
        unique = len(a) - max(counter_a.values()) + len(b) - max(counter_b.values())
        
        a_less_than_b = b_less_than_a = len(a) + len(b)
        
        # counter maintains a prefix sum and it adds up the frequency of all previous letters upto the letter being tried as boundary letter.
        for i in range(1,26):
            counter_a[i] += counter_a[i-1]
            counter_b[i] += counter_b[i-1]
            # cost to turn a less than b
            a_less_than_b = min(a_less_than_b, len(a) - counter_a[i] + counter_b[i])
            b_less_than_a = min(b_less_than_a, len(b) - counter_b[i] + counter_a[i])
        
        

        return min(a_less_than_b, b_less_than_a, unique)
      
------------------------------------------------------------------------------------------
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cn1, cn2 = [0] * 26, [0] * 26
        for c in a: cn1[ord(c)-97] += 1
        for c in b: cn2[ord(c)-97] += 1
        
        ans = len(a) + len(b) - max(x + y for x, y in zip(cn1, cn2)) # condition 3
        for i in range(1, 26):  # note that letters can't be smaller than 'a' or bigger than 'z'
            ans = min(ans, sum(cn1[:i]) + sum(cn2[i:]), sum(cn1[i:]) + sum(cn2[:i]))
        return ans
