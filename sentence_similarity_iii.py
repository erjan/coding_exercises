'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", 
"hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert
an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become 
equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made 
equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.
'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        # let s1 be the shorter sequence
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        # find the first index where they differ
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                break
            i += 1
        # check if the trailing part of s1 matches the end of s2
        return s1[i:] == s2[len(s2) - (len(s1) - i):]
      
-------------------------------------------------------------------

If the first words match, pop them out
If the last words match,pop them out
If neither matches, return False

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if(len(s1)>len(s2)):            #let s1 be the smaller and s2 be the greater
            s1,s2 = s2,s1
        while(s1): 
            if(s2[0]==s1[0]):
                s2.pop(0)
                s1.pop(0)
            elif(s2[-1]==s1[-1]):
                s2.pop()
                s1.pop()
            else:
                return(False)            
        return(True)
      
