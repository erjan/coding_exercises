#Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter
from collections import OrderedDict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        #print(freq)
        sorted_x = sorted(freq.items(),key = lambda x: x[1],reverse=True)
        sorted_x = dict(sorted_x)
        d = dict()
        for letter in s:
            if letter not in d.keys():
                d[letter] = 1
            else:
                d[letter]+=1
        print("dict freq is ")

        print(d)
        #print(sorted_x)
        d = sorted(d.items(), key = lambda x : x[1], reverse=True)
        string = ""
        for k, v in d:
            string+= k*v
        print(string)
        return string
