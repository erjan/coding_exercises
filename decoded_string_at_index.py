'''
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.
'''


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        lens = [0]
        
        for c in s:
            if c.isalpha():
                lens.append(lens[-1] + 1)
            else:
                lens.append(lens[-1] * int(c))
                
        for idx in range(len(s), 0, -1):
            k %= lens[idx]
            if k == 0 and s[idx - 1].isalpha():
                return s[idx - 1]
        
        return
