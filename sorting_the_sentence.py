'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
'''

#my own solution!


class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        q = dict()
        res = ''
        for i in range(len(s)):

            pos = int(s[i][-1]) - 1
            q[pos] = s[i][:-1]
            
        for i in range(len(s)):
            if i != len(s)-1:
                res += q[i] + ' '
            else:
                res += q[i]

       
        return res
    
    #better solution from submissions
    
    class Solution:
    def sortSentence(self, s: str) -> str:
        
        x = s.split()
        dic = {}
        for i in x :
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])

