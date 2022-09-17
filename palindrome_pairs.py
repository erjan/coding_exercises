'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

tl;dr

Iterate through words and map each to its index
For each word, generate all possible (left-hand-side) and (right-hand-side) that could form a palindrome with current word
Look up if we have a pair against the map in constant time
Handle edge case where current word is already a palindrome and we have an empty string in the wordList
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # keep a hashmap of word to its index
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        res = set()
        for i, word in enumerate(words):
            if not word:
                # we don't process empty string by itself
                continue
            
            # generate all possible LHS that would form
            # a palindrome with current word
            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((idx_map[target], i))
                    
            # generate all possible RHS that would form
            # a palindrome with current word
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((i, idx_map[target]))
                    
            # check if current word is already a palindrome and
            # if we have an empty string in our map
            if word == word[::-1] and "" in idx_map:
                idx = idx_map[""]
                res.add((i, idx))
                res.add((idx, i))

        return list(res)
