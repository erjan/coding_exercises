'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):                 
        deque = collections.deque([beginWord])
        ls = string.ascii_lowercase
        wordList = set(wordList)
        dist = 1
        while deque:
            size = len(deque)
            for _ in range(size): # BFS level by level
                word = deque.popleft()
                if word == endWord:
                    return dist
                for i in range(len(word)):
                    for c in ls:
                        if word[i] != c:
                            newWord = word[:i]+c+word[i+1:]
                            if newWord in wordList:
                                wordList.remove(newWord)
                                deque.append(newWord)
            dist += 1
        return 0
    
    def ladderLength1(self, beginWord, endWord, wordList):                 
        deque = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        wordList = set(wordList)
        while deque:
            word, dist = deque.popleft() # BFS one word by one word
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in ls:
                    if word[i] != c:
                        newWord = word[:i]+c+word[i+1:]
                        if newWord in wordList:
                            wordList.remove(newWord)
                            deque.append((newWord, dist+1))
        return 0
