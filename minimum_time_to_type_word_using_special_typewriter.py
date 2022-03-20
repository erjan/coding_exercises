'''
There is a special typewriter with lowercase English 
letters 'a' to 'z' arranged in a circle with a pointer. A character 
can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
'''

class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        
        last = 'a'
        
        for ch in word:
            
            val = (ord(ch) - ord(last) ) % 26
            
            total += min(val, 26-val)+1
            last = ch
        return total
