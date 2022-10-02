'''
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
'''

class Solution:
    def equalFrequency(self,word: str) -> bool:

        freq = list(Counter(word).values())
        if len(set(freq)) > 2: return False
        for i in range(len(freq)):
            freq[i] -= 1
            len_ = len(set(freq))
            if len_ == 1 or (len_ == 2 and freq[i] == 0):
                return True
            freq[i] += 1
        return False
----------------------------------------------------------------
class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        dic = Counter(word)
        count = Counter(dic.values())
        
        l1 = count.most_common()
        
		### here are some cases help you understand better  ###
        ###  like  abccc   abc ,aabbcc, aaa ###
        return (len(l1) == 2 and l1[-1][1] == 1 and abs(l1[0][0] -  l1[1][0]) == 1)\
                or (len(l1) == 1 and l1[0][0] == 1) or len(dic) == 1
