'''
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move 
any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

'''

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        d = dict()
        for i in range(len(words)):

            word = words[i]

            for letter in word:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] += 1

        print(d)
        num_words = len(words)

        d = list(d.values())

        print(d)

        for value in d:
            if value % num_words != 0:
                return False
        return True
