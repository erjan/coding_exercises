'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
'''

from collections import defaultdict
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def check(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
            return cnt == 1
        wordList.append(beginWord)
        if endWord not in wordList: return []
        wordList = list(set(wordList))
        G = defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                v, w = wordList[i], wordList[j]
                if check(v,w):
                    G[v].add(w)
                    G[w].add(v)
        #using BFS to construct predecessor array
        que = deque([(beginWord,0)])
        pred = defaultdict(list)
        visited = set()
        dist = defaultdict(lambda:float('inf'))
        while que:
            v, d = que.popleft()
            if v == endWord: break
            if v in visited: continue
            visited.add(v)
            for w in G[v]:
                if w not in visited:
                    if dist[w] == float('inf'):
                        dist[w] = d + 1
                        que.append((w,d+1))
                    if dist[w] == d+1:
                        pred[w].append(v)
        #enumerating all the shortest paths using backtracking
        res = []
        def dfs(v, path, goal):
            path.append(v)
            if v == goal:
                res.append(list(reversed(path)))
            for w in pred[v]:
                dfs(w, path, goal)
            path.pop()
        dfs(endWord, [], beginWord)
        return res
