'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.
'''


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        s = sentence
        s = s.split(' ')
        if len(s) == 1:

            if s[0][0] == s[0][-1]:
                return True
            else:
                return False
        
        for i in range(len(s)-1):
            w1 = s[i]
            w2 = s[i+1]

            if i == 0:
                if s[i][0] != s[-1][-1]:
                    return False

            if w1[-1] != w2[0]:
                return False
        return True

---------------------------------------------------------------------------------------------------------------
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        s = sentence
        s = s.split(' ')
        if len(s) == 1:

            if s[0][0] == s[0][-1]:
                return True
            else:
                return False
        
        for i in range(len(s)-1):
            w1 = s[i]
            w2 = s[i+1]

            if i == 0:
                if s[i][0] != s[-1][-1]:
                    return False

            if w1[-1] != w2[0]:
                return False
        return True

