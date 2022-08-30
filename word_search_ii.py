'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed 
from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''


import collections


class TrieNode():
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()
        self.numwords = 0
    
    def insert(self,word):
        node = self.root
        for w in word:
            node= node.children[w]
        node.isWord = True
        self.numwords +=1

class Solution(object):
    def dfs(self,i,j,trie,node,board,word,res):
        if not node or trie.numwords == 0:
            return
        
        if node.isWord:
            res.append(word)
            node.isWord = False
            trie.numwords -=1
        
        tmp = board[i][j]
        board[i][j] = '#'

        if i +1 < len(board):
            c = board[i+1][j]
            self.dfs(i+1,j,trie,node.children.get(c),board,word+c,res)
        
        if i -1 >=0:
            c = board[i-1][j]
            self.dfs(i-1,j,trie,node.children.get(c),board,word+c,res)

        if j+1 < len(board[0]):
            c = board[i][j+1]
            self.dfs(i,j+1,trie,node.children.get(c),board,word+c,res)
        
        if j-1 >=0:
            c = board[i][j-1]
            self.dfs(i,j-1,trie,node.children.get(c),board,word+c,res)
        
        board[i][j] = tmp
    
    def findWords(self,board,words):

        res = []

        trie = Trie()
        node = trie.root

        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i,j,trie,node.children[board[i][j]], board,board[i][j],res)
        
        return res
